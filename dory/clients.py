"""
Clients definition for Dory
"""
import datetime
from typing import Protocol, Optional, Any, List, Union


class Client(Protocol):
    """
    Engine definition standard.
    Other engines should inherit from it.
    """

    def get(self, key: str, default: Optional[str] = None) -> Any:
        """
        Fetch a given key from the cache.
        If the key does not exist, return default.
        """
        raise NotImplementedError

    def set(self, key: str, value: Any, expiration: Optional[datetime.timedelta]) -> None:
        """
        Set a value in the cache. If timeout is given, use that timeout for the
        key; otherwise use the default cache timeout.
        Return
        """
        raise NotImplementedError

    def touch(self, key: str) -> bool:
        """
        Expire a single key from the cache.
        Return whether if the operation succeeded or not.
        """
        raise NotImplementedError

    def touch_all(self, keys: List[str]) -> None:
        """
        Expire multiple keys from the cache.
        """
        raise NotImplementedError


    def delete(self, key: str) -> bool:
        """
        Delete a single key from the cache.
        Return whether it succeeded or not.
        """
        raise NotImplementedError

    def delete_all(self, keys: List[str]) -> bool:
        """
        Delete multiple keys from the cache
        """
        raise NotImplementedError

    def raw(self, command: str) -> Any:
        """
        Execute a raw command
        """
        raise NotImplementedError

    def ping(self) -> bool:
        """
        Check server availability
        """
        raise NotImplementedError