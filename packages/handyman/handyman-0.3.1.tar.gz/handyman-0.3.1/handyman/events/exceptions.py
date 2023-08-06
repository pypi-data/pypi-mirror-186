from handyman.exceptions import ErrorCodes, BaseError

class SQSErrorCodes(ErrorCodes):
    UNKNOWN = 3  # Unknown error
    QUEUE_DOES_NOT_EXIST = 4 # SQS QueueDoesNotExist
    CLIENT_INTERNAL_ERROR = 5 # SQS Client Internal Error
    CLIENT_UNKNOWN_ERROR = 6 # SQS Client Unknown Error - custom

class SQSException(BaseError):
    error_codes = SQSErrorCodes
