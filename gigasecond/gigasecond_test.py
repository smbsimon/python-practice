from datetime import datetime
import unittest

from gigasecond import add_gigasecond


class GigasecondTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            datetime(2043, 1, 1, 1, 46, 40),
            add_gigasecond(datetime(2011, 4, 25))
        )

    def test_2(self):
        self.assertEqual(
            datetime(2009, 2, 19, 1, 46, 40),
            add_gigasecond(datetime(1977, 6, 13))
        )

    def test_3(self):
        self.assertEqual(
            datetime(1991, 3, 27, 1, 46, 40),
            add_gigasecond(datetime(1959, 7, 19))
        )

    def test_4(self):
        self.assertEqual(
            datetime(2046, 10, 2, 23, 46, 40),
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0))
        )

    def test_5(self):
        self.assertEqual(
            datetime(2046, 10, 3, 1, 46, 39),
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59))
        )

if __name__ == '__main__':
    unittest.main()
