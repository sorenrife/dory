"""
Test Dory cache clients
"""
import unittest

from dory.config import settings
from dory.setup import setup as dory_setup
from dory import engines


class Redis(unittest.TestCase):
    """
    Test Redis client
    """

    def setUp(self) -> None:
        self.client = dory_setup(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            user=settings.REDIS_USER,
            password=settings.REDIS_PASSWORD,
            engine=engines.Redis,
        )

    def test_ping(self) -> None:
        """
        Test ping method
        """
        assert self.client.ping()

    def test_set(self) -> None:
        """
        Test set method
        """
        assert self.client.set("foo", "bar")

    def test_get(self) -> None:
        """
        Test get method
        """
        assert self.client.set("foo", "bar")
        assert self.client.get("foo"), b"bar"

    def test_touch(self) -> None:
        """
        Test touch method
        """
        assert self.client.set("foo", "bar")
        self.client.touch("foo")

    def test_raw(self) -> None:
        """
        Test raw method
        """
        assert self.client.raw("SET foo bar")
        assert self.client.get("foo") == b"bar"

    def test_delete(self) -> None:
        """
        Test delete method
        """
        assert self.client.set("foo", "bar")
        assert self.client.get("foo"), b"bar"
        self.client.delete("foo")
        assert self.client.get("foo"), None
