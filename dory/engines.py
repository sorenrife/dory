"""
Engines definition for Dory
"""
import redis

from typing import Protocol, Optional
from . import clients


class Engine(Protocol):
    """
    Engine definition standard.
    Other engines should inherit from it.
    """

    client: clients.Client

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: Optional[str] = None,
    ) -> None:
        raise NotImplementedError

class Redis(Engine):
    """
    Implementation of Redis engine
    """
    client: clients.Redis

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: Optional[str] = None,
    ) -> None:
        self.client = clients.Redis(
            rclient=redis.Redis(
                host=host,
                port=port,
                password=password,
                socket_connect_timeout=0.1,
                socket_timeout=0.2,
                retry_on_timeout=False,
            )
        )

engine: Engine