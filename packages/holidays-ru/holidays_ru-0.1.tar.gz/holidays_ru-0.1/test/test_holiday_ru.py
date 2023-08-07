import unittest
from datetime import date

from holidays_ru import check_holiday, is_holiday


class TestBasics(unittest.TestCase):
    def test_days(self):
        self.assertTrue(check_holiday(date(2023, 1, 1)))
        self.assertFalse(check_holiday(date(2023, 1, 12)))  # False
        self.assertTrue(check_holiday(date(2022, 12, 31)))
        self.assertFalse(
            check_holiday(date(2022, 12, 31), with_weekends=False)
        )  # False, it's Sunday
        self.assertEqual(
            is_holiday(date(2023, 1, 1)), "Новогодние каникулы"
        )  # "New Year's Day"
        self.assertEqual(is_holiday(date(2023, 1, 12)), "")  # ""
        self.assertEqual(
            is_holiday(date(2023, 1, 15)), "Выходной"
        )  # "Weekend"
        self.assertEqual(
            is_holiday(date(2021, 12, 31)), "Передвинутый выходной"
        )  # "Moved weekend"
        self.assertEqual(
            is_holiday(date(2023, 1, 12)), ""
        )  # "", it's work Sunday
