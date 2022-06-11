"""
General application health check
"""
import unittest

class Health(unittest.TestCase):

    def test_health(self) -> None:
        """
        Healthcheck
        """
        assert True