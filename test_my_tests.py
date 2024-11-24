import unittest

class MyTestCases(Unittest.TestCase):
    def test_check_number(self):
        self.assertEqual (check_number(3), "Odd")
        self.assertEqual(check_number(4), "Not Weird")
        self.assertEqual(check_number(6), "Weird")
        self.assertEqual(check_number(-4), "Not Weird")
        self.assertEqual(check_number(22), "Not Weird")
        self.assertEqual(check_number(-5), "Odd")
        self.assertEqual(check_number(0), "Neutral")

    if __name__ == "main":
        unittest.main
        