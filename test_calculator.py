"""
Unit tests for the calculator module.
"""
import unittest
from calculator import add, subtract, multiply, divide, power


class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations."""
    
    def test_add(self):
        """Test addition operation."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5.5, 2.5), 3.0)
    
    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 2), 5.0)
    
    def test_divide(self):
        """Test division operation."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-4, 2), -2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(7.5, 2.5), 3.0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(4, 0.5), 2.0)


if __name__ == "__main__":
    unittest.main()
