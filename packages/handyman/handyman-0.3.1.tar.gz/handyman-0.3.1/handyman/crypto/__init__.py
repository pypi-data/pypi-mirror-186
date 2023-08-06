import os
from typing import Union

# Declare env vars
ENCRYPTED_DATA_KEY = os.environ.get('ENCRYPTED_DATA_KEY', None)
VAULT_URI = os.environ.get('VAULT_URI', None)
VAULT_ROLE_ID = os.environ.get('VAULT_ROLE_ID', None)
VAULT_SECRET_ID = os.environ.get('VAULT_SECRET_ID', None)
VAULT_APPROLE_MOUNTPATH = os.environ.get('VAULT_APPROLE_MOUNTPATH', 'approle-batch')
VAULT_DATA_KEY_NAME = os.environ.get('VAULT_DATA_KEY_NAME', None)
PLAINTEXT_DATAKEY: Union[bytes, None] = None

from .vault import *
from .crypto import *
from .exceptions import *
