import unittest
import my_date

class MyDateTest(unittest.TestCase):

    def test_divided_by_4(self):
        self.assertTrue(my_date.is_leap_year(2040))
        self.assertTrue(my_date.is_leap_year(2016))
        self.assertTrue(my_date.is_leap_year(3200))

    def test_divided_by_100_and_400(self):
        self.assertTrue(my_date.is_leap_year(1600))
        self.assertTrue(my_date.is_leap_year(2800))

    def test_divided_by_100_but_not_400(self):
        self.assertFalse(my_date.is_leap_year(1700))
        self.assertFalse(my_date.is_leap_year(2300))

    def test_not_divided_by_4(self):
        self.assertFalse(my_date.is_leap_year(2027))
        self.assertFalse(my_date.is_leap_year(1997))

   
    def test_jan_1(self):
        self.assertEqual(my_date.ordinal_date(2023, 1, 1), 1)

    def test_feb_15(self):
        self.assertEqual(my_date.ordinal_date(2023, 2, 15), 46)

    def test_feb_29(self):
        self.assertEqual(my_date.ordinal_date(2024, 2, 29), 60)

    def test_dec_31(self):
        self.assertEqual(my_date.ordinal_date(2023, 12, 31), 365)

    def test_same_dates(self):
        self.assertEqual(my_date.days_elapsed(2023, 7, 24, 2023, 7, 24), 0)

    def test_consecutive_dates(self):
        self.assertEqual(my_date.days_elapsed(2023, 7, 23, 2023, 7, 24), 1)

    def test_same_year_dates(self):
        self.assertEqual(my_date.days_elapsed(2023, 7, 23, 2023, 12, 31), 161)

    def test_different_years(self):
        self.assertEqual(my_date.days_elapsed(2023, 9, 22, 2024, 9, 22), 366)

    def test_leapyear_dates(self):
        self.assertEqual(my_date.days_elapsed(2024, 2, 29, 2024, 12, 31), 306)
    
    def test_monday(self):
        self.assertEqual(my_date.day_of_week(2023, 9, 25), "Monday")

    def test_sunday(self):
        self.assertEqual(my_date.day_of_week(2023, 9, 18), "Monday")

    def test_saturday(self):
        self.assertEqual(my_date.day_of_week(2023, 9, 23), "Saturday")

    def test_wednesday(self):
        self.assertEqual(my_date.day_of_week(2022, 12, 7), "Wednesday")

    def test_thursday(self):
        self.assertEqual(my_date.day_of_week(2024, 2, 29), "Thursday")

    def test_friday(self):
        self.assertEqual(my_date.day_of_week(2025, 8, 15), "Friday")

    def test_tuesday(self):
        self.assertEqual(my_date.day_of_week(2000, 5, 2), "Tuesday")

    def test_monday(self):
        self.assertEqual(my_date.to_str(2023, 9, 18), "Monday, 18 September 2023")

    def test_tuesday(self):
        self.assertEqual(my_date.to_str(2023, 9, 19), "Tuesday, 19 September 2023")

    def test_wednesday(self):
        self.assertEqual(my_date.to_str(2023, 9, 20), "Wednesday, 20 September 2023")

    def test_thursday(self):
        self.assertEqual(my_date.to_str(2023, 9, 21), "Thursday, 21 September 2023")

    def test_friday(self):
        self.assertEqual(my_date.to_str(2023, 9, 22), "Friday, 22 September 2023")

    def test_saturday(self):
        self.assertEqual(my_date.to_str(2023, 9, 23), "Saturday, 23 September 2023")




if __name__ == '__main__':
    unittest.main()