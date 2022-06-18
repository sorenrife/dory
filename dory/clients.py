"""
Clients definition for Dory
"""
from typing import Protocol

class Client(Protocol):
    """
    Engine definition standard.
    Other engines should inherit from it.
    """