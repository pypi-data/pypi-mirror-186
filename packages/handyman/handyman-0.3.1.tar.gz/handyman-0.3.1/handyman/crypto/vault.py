import os
from typing import Any, Callable, Union
import hvac
from functools import wraps

import requests

from handyman.crypto.exceptions import VaultException, VaultErrorCodes, handle_vault_exceptions
from handyman.crypto import (
    ENCRYPTED_DATA_KEY,
    VAULT_URI,
    VAULT_ROLE_ID,
    VAULT_SECRET_ID,
    VAULT_APPROLE_MOUNTPATH,
    VAULT_DATA_KEY_NAME,
    PLAINTEXT_DATAKEY
)


VAULT_CLIENT = None

# Initialize Vault Client
@handle_vault_exceptions
def vault_client_init():
    """
    Function to initialize Vault Client
    """

    global VAULT_CLIENT

    VAULT_CLIENT = hvac.Client(
        url=VAULT_URI,
    )

# Login with approle auth
@handle_vault_exceptions
def vault_client_login():
    """
    Function to perform vault client login
    """

    global VAULT_CLIENT

    try:
        VAULT_CLIENT.auth.approle.login(
            role_id=VAULT_ROLE_ID,
            secret_id=VAULT_SECRET_ID,
            mount_point=VAULT_APPROLE_MOUNTPATH,
        )
    except requests.exceptions.ConnectionError:
        # Vault connection cant be made
        raise VaultException(VaultErrorCodes.CONNECTION_ERROR, f'Connection with Vault failed, please check if url "{VAULT_URI}" is correct / live')
    except hvac.exceptions.Forbidden:
        # Login failed - login path incorrect / other permission issues
        raise VaultException(VaultErrorCodes.LOGIN_PATH_ERROR, f'Vault login error, check if login path "{VAULT_APPROLE_MOUNTPATH}" is enabled.')
    except (hvac.exceptions.InvalidRequest, hvac.exceptions.InvalidPath):
        # Login failed - role_id or secret_id incorrect
        raise VaultException(VaultErrorCodes.UNAUTHENTICATED, 'Vault login failed, vault credentials incorrect.')
    except Exception as e:
        raise VaultException(VaultErrorCodes.UNKNOWN, 'Unknown error occurred during Vault login') from e

@handle_vault_exceptions
def check_vault_authenticated() -> bool:
    """
    Check if Vault client is authenticated

    :return bool: vault authentication status as boolean
    """

    global VAULT_CLIENT

    is_authenticated = False

    if VAULT_CLIENT.is_authenticated():
        is_authenticated = True

    return is_authenticated

def token_refresh(wrapped: Callable[..., Any]):
    """
    Decorator function to refresh token when wrapped function encounters a code which returns unauthorized from vault
    """

    # Initilize Vault Client if not done earlier
    if not VAULT_CLIENT:
        vault_client_init()

    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to check for vault unauthorized, refresh token if so
        """

        # Login and get token if no token present
        if check_vault_authenticated():
            vault_client_login()

        try:
            response = wrapped(*args, **kwargs)
        except hvac.exceptions.Forbidden:
            # Retry login in case token expires and re-run wrapped function
            vault_client_login()

            response = wrapped(*args, **kwargs)

        return response

    return wrapper

# Functions for transit keys management

@handle_vault_exceptions
@token_refresh
def transit_key_exist(key_name: str) -> bool:
    """
    Check if transit path exists

    :param str key_name: name of the transit path to check for existence
    :return bool: true is path exists, false if doesn't
    """

    key_exists = False

    try:
        VAULT_CLIENT.secrets.transit.read_key(key_name)

        key_exists = True
    except hvac.exceptions.InvalidPath:
        # Key does not exist
        pass

    return key_exists

@handle_vault_exceptions
@token_refresh
def transit_create_key(key_name: str):
    """
    Create a new transit key (ie a new transit path in vault)

    :param str key_name: name of the transit path to create
    """

    # TBD: allow_plaintext_backup parameter
    try:
        VAULT_CLIENT.secrets.transit.create_key(key_name, key_type='aes256-gcm96')
    except hvac.exceptions.Forbidden:
        # Login failed - login path incorrect / other permission issues
        raise VaultException(VaultErrorCodes.UNAUTHORIZED, f'Vault client unauthorized to create new transit keys, check approle permissions.')

@handle_vault_exceptions
@token_refresh
def transit_delete_key(key_name: str):
    """
    TODO: Delete encryption key from cache after deletion from vault, else encryption will still be available for the client till process restarts
    Delete transit key
    NOTE: Use with caution, once deleted, data key can no longer be decrypted and all encrypted data would be lost

    :param str key_name: name of the transit key to delete
    """

    # If key not present, return
    if not transit_key_exist(key_name):
        return

    # Enable key deletion by updating configuration
    try:
        VAULT_CLIENT.secrets.transit.update_key_configuration(key_name, deletion_allowed=True)
    except hvac.exceptions.Forbidden:
        # Login failed - login path incorrect / other permission issues
        raise VaultException(VaultErrorCodes.UNAUTHORIZED, f'Vault client unauthorized to update transit key configurations, check approle permissions.')

    # Delete the key
    try:
        VAULT_CLIENT.secrets.transit.delete_key(key_name)
    except hvac.exceptions.Forbidden:
        # Login failed - login path incorrect / other permission issues
        raise VaultException(VaultErrorCodes.UNAUTHORIZED, f'Vault client unauthorized to delete transit keys, check approle permissions.')

# Functions for encryption and decryption

@handle_vault_exceptions
@token_refresh
def transit_decrypt_data(transit_path: str, ciphertext: str) -> str:
    """
    Decrypt data at particular transit path.

    :param str transit_path: name of the transit key for decryption
    :param str ciphertext: encrypted data to decrypt
    :return str: decrypted data as plaintext
    """

    global VAULT_CLIENT

    decrypt_data_response = VAULT_CLIENT.secrets.transit.decrypt_data(
        name = transit_path,
        ciphertext = ciphertext,
    )

    if not isinstance(decrypt_data_response, dict):
        raise VaultException(VaultErrorCodes.EMPTY_RESPONSE, "Response from Vault is not a dict")

    try:
        decrypted_data: str = decrypt_data_response["data"]["plaintext"]
    except (KeyError, TypeError):
        raise VaultException(VaultErrorCodes.EMPTY_RESPONSE, "Empty response from Vault while decrypting ciphertext.")

    return decrypted_data

@handle_vault_exceptions
@token_refresh
def transit_generate_data_key(transit_path: str) -> str:
    """
    Generate data key at given transit path.

    :param str transit_path: transit key path
    :return str: encrypted data key as string
    """

    global VAULT_CLIENT

    # Generate a new high entropy data key
    response: dict = VAULT_CLIENT.secrets.transit.generate_data_key(transit_path, "wrapped", bits=256)

    if not isinstance(response, dict):
        raise VaultException(VaultErrorCodes.EMPTY_RESPONSE, "Response from Vault, while generating data key, is not a dict")

    try:
        encrypted_data_key: str = response["data"]["ciphertext"]
    except (KeyError, TypeError):
        raise VaultException(VaultErrorCodes.EMPTY_RESPONSE, "Empty response from Vault, no/incorrect data present in the response of generate data key api of Vault.")

    return encrypted_data_key

@handle_vault_exceptions
@token_refresh
def transit_read_key(transit_path: str) -> Union[dict, None]:
    """
    Read config data at transit path.

    :param str transit_path: transit key path
    :return str: encrypted data key as string
    """

    global VAULT_CLIENT

    try:
        response_: dict = VAULT_CLIENT.secrets.transit.read_key(transit_path)
    except hvac.exceptions.Forbidden:
        # Login failed - login path incorrect / other permission issues
        raise VaultException(VaultErrorCodes.UNAUTHORIZED, f'Vault client unauthorized to read transit keys, check approle permissions.')

    if not isinstance(response_, dict):
        raise VaultException(VaultErrorCodes.EMPTY_RESPONSE, "Response from Vault, while reading transit key configuration, is not a dict")

    try:
        configuration: Union[dict, None] = response_["data"]
    except KeyError:
        raise VaultException(VaultErrorCodes.EMPTY_RESPONSE, "Empty response from Vault, transit configuration data not found")

    return configuration
