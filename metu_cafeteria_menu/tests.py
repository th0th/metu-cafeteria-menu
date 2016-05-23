import unittest
from metu_cafeteria_menu import fetch


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
        with self.assertRaises(ValueError):
            menu = fetch('2016-05-21')

if __name__ == '__main__':
    unittest.main()
