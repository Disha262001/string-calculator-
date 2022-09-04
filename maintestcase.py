import unittest
from main import StringCalculator

class StringCalculatorTestCase(unittest.TestCase):
    stringCal = StringCalculator()

    def test_for_null_string(self):

        result = self.stringCal.add("")
        self.assertEqual(result, 0)

        result1 = self.stringCal.add("2")
        self.assertEqual(result1, 2)

        result2 = self.stringCal.add("22")
        self.assertEqual(result2, 22)


