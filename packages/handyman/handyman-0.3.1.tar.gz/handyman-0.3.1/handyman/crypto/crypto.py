from base64 import b64decode, b64encode
import os
from typing import Tuple, Union

import hvac
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

from handyman.crypto import (
    ENCRYPTED_DATA_KEY,
    VAULT_DATA_KEY_NAME,
    PLAINTEXT_DATAKEY,
)
from handyman.crypto.vault import (
    transit_create_key,
    token_refresh,
    transit_generate_data_key,
    transit_key_exist,
    transit_decrypt_data,
    transit_read_key,
)
from handyman.log import get_logger
from handyman.crypto.cache import cache
from handyman.crypto.exceptions import CryptoErrorCodes, CryptoException, VaultException, VaultErrorCodes
from handyman.helpers import return_exception_as_parameter


LOGGER = get_logger("crypto")
# Global datakey name override if VAULT_DATA_KEY_NAME does not exist
GLOBAL_DATA_KEY_NAME_OVERRIDE = "global"

@token_refresh
def get_plaintext_datakey(client_id: str = None, data_key: str = None, disable_cache: bool = False) -> Union[str, None]:
    """
    Function to decrypt the encrypted data key using Vault Client

    :param str client_id: client uuid
    :param str data_key: encrypted data key
    :return bytes | None: plaintext datakey in bytes
    """

    global VAULT_DATA_KEY_NAME
    global ENCRYPTED_DATA_KEY
    global PLAINTEXT_DATAKEY

    # Check cache for available plaintext key
    if not disable_cache and client_id and cache.exists(client_id):
        return cache.get(client_id)
    elif not disable_cache \
        and not client_id \
        and cache.exists(VAULT_DATA_KEY_NAME or GLOBAL_DATA_KEY_NAME_OVERRIDE):
        return cache.get(VAULT_DATA_KEY_NAME or GLOBAL_DATA_KEY_NAME_OVERRIDE)

    # Decrypt the encrypted data key
    transit_path = client_id or VAULT_DATA_KEY_NAME
    ciphertext = data_key or ENCRYPTED_DATA_KEY

    decrypted_key_b64encoded = transit_decrypt_data(transit_path, ciphertext)

    try:
        # Base64 decode decrypted_key
        decrypted_key = b64decode(decrypted_key_b64encoded)
    except Exception as e:
        LOGGER.error(e)
        raise CryptoException(CryptoErrorCodes.B64_ENCODE_ERROR, 'Base64 encoded data key cant be converted to bytes, incorrect encoding.')

    # Set cache
    if  not disable_cache and client_id:
        cache.set(client_id, decrypted_key)
    elif not disable_cache:
        cache.set(VAULT_DATA_KEY_NAME or GLOBAL_DATA_KEY_NAME_OVERRIDE, decrypted_key)

    # Set the global variable to decrypted value, if client_id not passed
    if not client_id:
        PLAINTEXT_DATAKEY = decrypted_key

    return decrypted_key

@return_exception_as_parameter
@token_refresh
def generate_new_data_key(client_id: str) -> Tuple[Union[str, None], Union[Exception, None]]:
    """
    Function to generate a new data key, from the transit path as client_id.
    This creates the transit path for passed client_id if doesn't exist

    :param str client_id: client_id to generate the data key for
    :return str | None: generated data key as base64 encoded string
    """

    if not transit_key_exist(client_id):
        # Create transit key path if key path does not exist
        transit_create_key(client_id)
    else:
        # Check if key has correct configuration
        configuration = transit_read_key(client_id)

        try:
            # If key does not have correct configuration, return
            if configuration["type"] != 'aes256-gcm96' and configuration["auto_rotate_period"] != 0:
                raise VaultException(VaultErrorCodes.INCORRECT_CONFIGURATION, f'Already existing transit key "{client_id}" is not configured correctly, please check configuration before generating data key')
        except TypeError:
            raise VaultException(VaultErrorCodes.EMPTY_RESPONSE, "Empty response from Vault, transit configuration data not found")

    # Generate a new high entropy data key
    encrypted_data_key: str = transit_generate_data_key(client_id)

    return encrypted_data_key


def decrypt_bytes_(
    encrypted_data: bytes,
    client_id: str = None,
    data_key: str = None,
    decode_to_str: bool = False,
    disable_cache: bool = False,
) -> Tuple[Union[bytes, str, None], Union[Exception, None]]:
    """
    Function to decrypt incoming encrypted bytes to stream of bytes or string.
    Encryption algorithm used - AES-256 GCM mode (*256 optional, depends on keysize)

    :param bytes encrypted_data: encrypted data to be decrypted
    :param str client_id: client uuid
    :param str data_key: encrypted data key
    :param bool decode_to_str: decode to string boolean
    :param bool disable_cache: disable client's encryption key cache
    :return bytes | str: decrypted bytes or string returned
    """

    # Encryption key
    key = get_plaintext_datakey(client_id, data_key, disable_cache=disable_cache)
    if not key:
        raise CryptoException(CryptoErrorCodes.KEY_ERROR, 'Decryption key is null')

    try:
        # Initialization vector / nonce - keep it static 12 bytes always
        iv = encrypted_data[:12]
    except IndexError:
        raise CryptoException(CryptoErrorCodes.DECRYPTION_ERROR, 'Encrypted data too short to read the initialization vector bytes')

    try:
        # Actual encrypted data
        encrypted_data_contents = encrypted_data[12:-16]
    except IndexError:
        raise CryptoException(CryptoErrorCodes.DECRYPTION_ERROR, 'Encrypted data too short to read encryption contents')

    try:
        # Tag is the auth segment to be verified, 16 bytes standard
        tag = encrypted_data[-16:]
    except IndexError:
        raise CryptoException(CryptoErrorCodes.DECRYPTION_ERROR, 'Encrypted data too short to read the trailing tag data')


    try:
        # Create cipher object
        decryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
        ).decryptor()

        # Decryption gets us the authenticated plaintext.
        decrypted_bytes = decryptor.update(encrypted_data_contents) + decryptor.finalize()
    except Exception as e:
        LOGGER.error(e)
        raise CryptoException(CryptoErrorCodes.BAD_CIPHER, 'Cannot create stable cipher object for decrption from the given encrypted data.')

    result = decrypted_bytes

    # Decode to string if requested
    if decode_to_str:
        try:
            result = decrypted_bytes.decode("utf-8")
        except Exception as e:
            LOGGER.error(e)
            raise CryptoException(CryptoErrorCodes.UTF8_ENCODE_ERROR, 'Decrypted bytes cant be converted to utf-8')

    return result

@return_exception_as_parameter
def decrypt_bytes(
    encrypted_data: bytes,
    client_id: str = None,
    data_key: str = None,
    decode_to_str: bool = False,
    disable_cache: bool = False,
) -> Tuple[Union[bytes, str, None], Union[Exception, None]]:
    """
    Function to decrypt incoming encrypted bytes to stream of bytes or string.
    Uses decrypt_bytes to perform decryption operation

    :param bytes encrypted_data: encrypted data to be decrypted
    :param str client_id: client uuid
    :param str data_key: encrypted data key
    :param bool decode_to_str: decode to string boolean
    :param bool disable_cache: disable client's encryption key cache
    :return bytes | str: decrypted bytes or string returned
    """

    return decrypt_bytes_(encrypted_data, client_id, data_key, decode_to_str, disable_cache=disable_cache)

@return_exception_as_parameter
def decrypt_base64_string(
    encrypted_data_b64_str: str,
    client_id: str = None,
    data_key: str = None,
    decode_to_str: bool = False,
    disable_cache: bool = False,
) -> Tuple[Union[bytes, str, None], Union[Exception, None]]:
    """
    Function to decrypt incoming base64 encoded encrypted data to stream of bytes or string.
    Uses decrypt_bytes to perform decryption operation

    :param str encrypted_data_b64_str: base64 encoded encrypted data
    :param str client_id: client uuid
    :param str data_key: encrypted data key
    :param bool decode_to_str: decode to string boolean
    :param bool disable_cache: disable client's encryption key cache
    :return bytes | str: decrypted bytes or string returned
    """

    # Decode base64 encoded encrypted data into bytes
    try:
        encrypted_data_bytes = b64decode(encrypted_data_b64_str)
    except Exception as e:
        LOGGER.error(e)
        raise CryptoException(CryptoErrorCodes.B64_ENCODE_ERROR, 'Base64 encoded data cant be converted to bytes, incorrect encoding.')

    return decrypt_bytes_(encrypted_data_bytes, client_id, data_key, decode_to_str, disable_cache=disable_cache)


@return_exception_as_parameter
def encrypt_string(
    data: str,
    client_id: str = None,
    data_key: str = None,
    disable_cache: bool = False,
) -> Tuple[Union[str, None], Union[Exception, None]]:
    """
    Function to convert an incoming string into an encrypted stream of bytes.
    Encryption algorithm used - AES-256 GCM mode (*256 optional, depends on keysize)

    :param str data: string to be encrypted
    :param str client_id: client uuid
    :param str data_key: encrypted data key
    :param bool disable_cache: disable client's encryption key cache
    :return bytes: encrypted bytes
    """

    # Initialization vector / nonce - keep it static 12 bytes always
    iv = os.urandom(12)

    # Encryption key
    key = get_plaintext_datakey(client_id, data_key, disable_cache=disable_cache)
    if not key:
        raise CryptoException(CryptoErrorCodes.KEY_ERROR, 'Decryption key is null')

    try:
        # Construct an AES-GCM Cipher object with the given key and a
        # randomly generated IV.
        encryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, None, 16),
        ).encryptor()

        # Encrypt the plaintext and get the associated ciphertext.
        ciphertext = encryptor.update(bytes(data, "ascii")) + encryptor.finalize()
    except Exception as e:
        LOGGER.error(e)
        raise CryptoException(CryptoErrorCodes.BAD_CIPHER, 'Cannot create stable cipher object for decrption from the given encrypted data.')

    # Construct the full encrypted message
    encrypted_bytes = iv + ciphertext + encryptor.tag

    try:
        # Encode encrypted bytes to base64
        encrypted_str = b64encode(encrypted_bytes).decode('utf-8')
    except Exception as e:
        LOGGER.error(e)
        raise CryptoException(CryptoErrorCodes.B64_ENCODE_ERROR, 'Encrypted byte sequence cannot be converted into base64 string.')

    return encrypted_str
