import os
from typing import Union

# Declare env vars
AWS_REGION = os.environ.get('AWS_DEFAULT_REGION', None)
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)

from .sqs import *
from .event_types import *
