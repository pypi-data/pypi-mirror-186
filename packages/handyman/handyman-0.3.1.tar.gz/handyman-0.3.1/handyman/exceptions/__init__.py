import inspect
import sys
from abc import ABCMeta
from enum import EnumMeta, Enum


class BaseError(Exception, metaclass=ABCMeta):
    """
    Base exception to be used to handle exceptions
    """

    error_codes = None

    def __init__(self, error_code, message='', *args, **kwargs):
        """
        Creates a BaseException object.
        Any extending class must start their custom error code values from 2.

        :param ErrorCodes error_code: error code to be set on the exception
        :param str message: Message to be set on the exception
        :param args: args used to format the error message
        :param kwargs: kwargs used to format the error message
        """
        # Checking if the self.error_codes attribute is a class
        if not inspect.isclass(self.error_codes) and not isinstance(error_code, _ErrorCodes):
            raise BaseError(_ErrorCodes.ERROR_CODE_MISSING, 'The error_codes attribute must be a class.')

        # Checking if the self.error_codes attribute extends exceptions.ErrorCode
        if self.error_codes and \
                not issubclass(self.error_codes, ErrorCodes) and \
                not isinstance(error_code, _ErrorCodes):
            msg = 'The error_codes attribute must extend exceptions.ErrorCodes'
            raise BaseError(_ErrorCodes.ERR_INCORRECT_ERRCODE, msg)

        # Raise a separate exception in case the error code passed isn't specified in the ErrorCodes enum
        if (not isinstance(error_code, ErrorCodes) or
            (self.error_codes and not isinstance(error_code, self.error_codes))) and \
                not isinstance(error_code, _ErrorCodes):
            if self.error_codes == ErrorCodes:
                msg = "exceptions.ErrorCodes must be extended and it's values passed as the error code." \
                      " It cannot be set as the error codes to be used."
            else:
                msg = 'Error code passed in the error_code param must be of type "{0}"'
            raise BaseError(_ErrorCodes.ERR_INCORRECT_ERRCODE, msg, self.error_codes.__name__)

        # Storing the error code on the exception object
        self.error_code = error_code

        # storing the traceback which provides useful information about where the exception occurred
        self.traceback = sys.exc_info()

        # Prefixing the error code to the exception message
        try:
            msg = '[{0}] {1}'.format(error_code.name, message.format(*args, **kwargs))
        except (IndexError, KeyError):
            msg = '[{0}] {1}'.format(error_code.name, message)

        super().__init__(msg)


# Error codes for exceptions
class ErrorCodes(Enum, metaclass=EnumMeta):
    pass


class _ErrorCodes(ErrorCodes):
    ERROR_CODE_MISSING = 0  # There is no error code enum specified for the exception
    ERR_INCORRECT_ERRCODE = 1  # error code passed is not specified in enum ErrorCodes
    ERR_INCORRECT_LOGGER = 2  # Logger passed should be of type ESLogger
