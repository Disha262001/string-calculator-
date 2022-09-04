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

        result8 = self.stringCal.add("2,1001")
        self.assertEqual(result8, 2)

        result9 = self.stringCal.add("1005,99,100,05")
        self.assertEqual(result9, 204)

        result10 = self.stringCal.add("1\n2,3")
        self.assertEqual(result10, 6)

        result11= self.stringCal.add("//;\n1;2")
        self.assertEqual(result11, 4)





