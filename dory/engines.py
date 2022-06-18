"""
Engines definition for Dory
"""
from typing import Protocol, Optional
from .clients import Client


class Engine(Protocol):
    """
    Engine definition standard.
    Other engines should inherit from it.
    """

    client: Client

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: Optional[str] = None,
    ) -> None:
        pass
