"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test calc module    """
    def test_add_numbers(self):
        """Test sum fucntionality"""
        res=calc.add(5,6)

        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        """Test substraction fucntionality"""
        res=calc.substract(10,15)

        self.assertEqual(res,5)

