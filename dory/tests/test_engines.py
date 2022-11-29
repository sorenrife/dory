"""
Test Dory cache engines
"""
import unittest

from dory.config import settings
from dory.setup import setup as dory_setup
from dory import engines


class Redis(unittest.TestCase):
    """
    Test Redis client
    """

    def test_ping(self) -> None:
        client = dory_setup(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            user=settings.REDIS_USER,
            password=settings.REDIS_PASSWORD,
            engine=engines.Redis,
        )
        assert client.ping()