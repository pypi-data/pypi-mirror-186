from functools import wraps
from typing import Any, Callable
import hvac
import requests

from handyman.crypto import VAULT_URI
from handyman.exceptions import ErrorCodes, BaseError
from handyman.log import get_logger


LOGGER = get_logger()

class CryptoErrorCodes(ErrorCodes):
    UNKNOWN = 3  # Unknown error while encryption / decryption
    KEY_ERROR = 4 # Key for encryption / decryption not found or incorrect
    ENCRYPTION_ERROR = 5 # Error when encryption on a path with given plaintext fails
    DECRYPTION_ERROR = 6 # Error when decrytion on a path with given ciphertext fails
    BAD_CIPHER = 7 # Cipher object badly created
    UTF8_ENCODE_ERROR = 8 # Decrypted bytes cannot be converted to utf-8 codec or otherwise
    B64_ENCODE_ERROR = 9 # Decrypted bytes cannot be converted to base64 codec or otherwise

class VaultErrorCodes(ErrorCodes):
    UNAUTHENTICATED = 3  # Vault is Unauthenticated
    UNAUTHORIZED = 4  # Vault is Unauthenticated
    UNKNOWN = 5  # Unknown error from Vault Client
    EMPTY_RESPONSE = 6 # When returned response does not have data(or other relevant) keys
    DECRYPTION_API_ERROR = 7 # Error when decrytion on a path with given ciphertext fails
    CONNECTION_ERROR = 8 # Error in connecting with vault
    LOGIN_PATH_ERROR = 9 # Incorrect login path
    INCORRECT_CONFIGURATION = 10 # Incorrect configuration for given vault feature/entity
    INVALID_PATH = 11 # Incorrect request path

class VaultException(BaseError):
    error_codes = VaultErrorCodes

class CryptoException(BaseError):
    error_codes = CryptoErrorCodes

def handle_vault_exceptions(wrapped: Callable[..., Any]):
    """
    Decorator function to handle Vault related exceptions
    """

    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to handle Vault related exceptions
        """

        try:
            response = wrapped(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            # Connection to vault fail
            raise VaultException(VaultErrorCodes.CONNECTION_ERROR, f'Connection with Vault failed, please check if url "{VAULT_URI}" is correct / live')
        except hvac.exceptions.Forbidden:
            # Unauthorized
            raise VaultException(VaultErrorCodes.UNAUTHORIZED, f'Request made to vault is unauthorized, check if token is valid or client has sufficient permissions to access the resource.')
        except (hvac.exceptions.InvalidRequest, hvac.exceptions.InvalidPath):
            # Invalid path or unauthorized
            raise VaultException(VaultErrorCodes.INVALID_PATH, 'Request to vault made at invalid path or client is unauthorized to access the path.')
        except Exception as e:
            LOGGER.error(e)
            raise e

        return response

    return wrapper
