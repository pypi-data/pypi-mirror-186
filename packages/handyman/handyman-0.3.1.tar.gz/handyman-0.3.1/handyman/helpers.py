import time
import random

def retry_with_backoff(retries = 3, backoff_sec = 1):
    '''
    Function to retry a function with certain backoff seconds
    '''
    def wrapper(f):
        def wrapped(*args, **kwargs):
            i = 0
            while True:
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    if i >= retries:
                        raise e

                    sleep = (backoff_sec * 2 ** i + random.uniform(0, 1))
                    time.sleep(sleep)
                    i += 1

        return wrapped
    return wrapper

from functools import wraps
from typing import Any, Callable

def return_exception_as_parameter(wrapped: Callable[..., Any]):
    """
    Decorator function to return any raised exception in the wrapped function as last parameter parameter
    """

    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to catch any exception and return as last parameter
        """

        try:
            response = wrapped(*args, **kwargs), None
        except Exception as e:
            response = None, e

        return response

    return wrapper
