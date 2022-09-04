import unittest
from main import StringCalculator

class StringCalculatorTestCase(unittest.TestCase):
    stringCal = StringCalculator()

    def test_for_null_string(self):
        result = self.stringCal.add("")
        self.assertEqual(result, 0)
