import unittest
import datetime
from metu_cafeteria_menu import fetch
from metu_cafeteria_menu.exceptions import DateException


class TestCommonFunction(unittest.TestCase):
    def test_default(self):
        """Get the menu for 2016-05-20."""
        menu = fetch('2016-05-20')

        self.assertEqual(len(menu.get('lunch').get('menu')), 4)
        self.assertEqual(len(menu.get('dinner').get('menu')), 4)
        self.assertEqual(len(menu.get('alacarte').get('menu')), 18)
        self.assertEqual(len(menu.get('social_building').get('menu')), 17)

    def test_weekend(self):
        """Raise a ValueError if selected date is on weekend."""
        with self.assertRaises(DateException):
            menu = fetch('2016-05-21')

    def test_invalid_date(self):
        """Raise a ValueError if date is in invalid format."""
        with self.assertRaises(ValueError):
            menu = fetch('123-123-123')

    def test_default_date(self):
        """Without a date defined, the function should use the today's date."""
        default_menu, default_exception, todays_menu, todays_exception = None, None, None, None

        try:
            default_menu = fetch()
        except Exception as e:
            default_exception = e

        try:
            todays_menu = fetch(datetime.datetime.now().strftime('%Y-%m-%d'))
        except Exception as e:
            todays_exception = e

        self.assertEqual(default_menu, todays_menu)
        self.assertEqual(default_exception, todays_exception)


if __name__ == '__main__':
    unittest.main()
