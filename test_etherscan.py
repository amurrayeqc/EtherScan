# test_etherscan.py
"""
Tests for EtherScan module.
"""

import unittest
from etherscan import EtherScan

class TestEtherScan(unittest.TestCase):
    """Test cases for EtherScan class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherScan()
        self.assertIsInstance(instance, EtherScan)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherScan()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
