from typing import Dict

# Define a singleton metaclass
class Singleton(type):
    """
    This is a singleton metaclass implementation, ie makes sure all classes with this as a metaclass has only one instance created
    """

    def __init__(self, *args, **kwargs):
        self.__instances = {}
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class Cache(metaclass=Singleton):
    """
    A class implementing a simple dictionary cache, mapping string to bytes
    """

    def __init__(self):
        self.__cache: Dict[str, bytes] = {}

    def get(self, key: str):
        """
        get value of a key from cache
        """
        return self.__cache.get(key)

    def set(self, key: str, value: bytes):
        """
        set value against a key in cache
        """
        self.__cache[key] = value

    def exists(self, key):
        """
        checks if key exists in cache
        """
        exists = False

        if key in self.__cache:
            exists = True

        return exists

    def get_cache(self):
        """
        return whole cache dict
        """
        return self.__cache

cache = Cache()
