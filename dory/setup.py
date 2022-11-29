"""
Setup Dory
"""
from typing import Union, Optional, Type

from . import clients, engines


def setup(
    host: str,
    port: int,
    user: str,
    password: Optional[str] = None,
    engine: Type[engines.Engine] = engines.Redis,
) -> clients.Client:
    """
    Setup Dory
    """
    _engine = engine(
        host=host,
        port=port,
        user=user,
        password=password,
    )

    # setup environment variables
    setattr(engines, "engine", _engine)
    setattr(clients, "client", _engine.client)
    return clients.client
