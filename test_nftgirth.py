# test_nftgirth.py
"""
Tests for NftGirth module.
"""

import unittest
from nftgirth import NftGirth

class TestNftGirth(unittest.TestCase):
    """Test cases for NftGirth class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftGirth()
        self.assertIsInstance(instance, NftGirth)

    def test_run_method(self):
        """Test the run method."""
        instance = NftGirth()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
