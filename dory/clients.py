"""
Clients definition for Dory
"""
import datetime
from typing import Protocol, Optional, Any, List, Union

import redis


class Client(Protocol):
    """
    Client definition standard.
    Other clients should inherit from it.
    """

    def get(self, key: str, default: Optional[str] = None) -> Any:
        """
        Fetch a given key from the cache.
        If the key does not exist, return default.
        """
        raise NotImplementedError

    def set(
        self, key: str, value: Any, expiration: Optional[datetime.timedelta] = None
    ) -> bool:
        """
        Set a value in the cache. If timeout is given, use that timeout for the
        key; otherwise use the default cache timeout.
        Return
        """
        raise NotImplementedError

    def touch(self, keys: Union[str, List[str]]) -> int:
        """
        Expire multiple keys from the cache.
        Return number of succeeded operations.
        """
        raise NotImplementedError

    def delete(self, keys: Union[str, List[str]]) -> int:
        """
        Delete multiple keys from the cache.
        Return number of succeeded operations.
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


class Redis(Client):
    """
    Redis client implementation
    """

    rclient: redis.Redis

    def __init__(self, rclient: redis.Redis):
        self.rclient = rclient

    def get(self, key: str, default: Optional[str] = None) -> Any:
        """
        Redis implementation for `get`
        """
        result = self.rclient.get(name=key)
        return result if result else default

    def set(
        self, key: str, value: Any, expiration: Optional[datetime.timedelta] = None
    ) -> bool:
        """
        Redis implementation for `set`
        """
        return self.rclient.set(name=key, value=value, ex=expiration) or False

    def touch(self, keys: Union[str, List[str]]) -> int:
        """
        Redis implementation for `touch`
        """
        return self.rclient.touch(*keys if isinstance(keys, list) else keys)  # type: ignore

    def delete(self, keys: Union[str, List[str]]) -> int:
        """
        Redis implementation for `delete`
        """
        return self.rclient.delete(*keys if isinstance(keys, list) else keys)

    def raw(self, command: str) -> Any:
        """
        Redis implementation for `raw`
        """
        return self.rclient.execute_command(command)

    def ping(self) -> bool:
        """
        Redis implementation for `ping`
        """
        return self.rclient.ping()


client: Client
