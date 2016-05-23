import datetime
import urllib.request
from bs4 import BeautifulSoup
from metu_cafeteria_menu.utils import to_title, to_upper, to_lower

config = {
    'base_url': "http://kafeterya.metu.edu.tr/",
    'req_path': "tarih/",
}


def fetch(date=None):
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')

    if date_obj.weekday() > 4:
        raise ValueError("Cafeteria works only on weekdays.")

    menus = {
        'lunch': {
            'status': None,
            'menu': [],
        },
        'dinner': {
            'status': None,
            'menu': [],
        },
        'alacarte': {
            'status': None,
            'menu': [],
        },
        'social_building': {
            'status': None,
            'menu': [],
        },
    }

    res = urllib.request.urlopen(
        config.get('base_url') + config.get('req_path') + date_obj.strftime('%d-%m-%Y')
    )

    soup = BeautifulSoup(res.read(), 'html.parser')

    all_menus = soup.find_all('div', {'class': 'yemek-listesi'})

    for single_menu in all_menus:
        if single_menu.find('h3').text == 'Öğle Yemeği':
            # lunch
            meals = single_menu.find_all('div', {'class': 'yemek'})

            if len(meals) > 0:
                for meal in meals:
                    menus['lunch']['menu'].append({
                        'title': to_title(meal.find('p').contents[0]),
                        'img': '%s%s' % (
                            config.get('base_url'),
                            meal.find('img').get('src'),
                        )
                    })

        elif single_menu.find('h3').text == 'Akşam Yemeği':
            # dinner
            meals = single_menu.find_all('div', {'class': 'yemek'})

            if len(meals) > 0:
                for meal in meals:
                    menus['dinner']['menu'].append({
                        'title': to_title(meal.find('p').contents[0]),
                        'img': '%s%s' % (
                            config.get('base_url'),
                            meal.find('img').get('src'),
                        )
                    })
        elif single_menu.find('h3').text == 'Kafeterya Alakart':
            # alacarte
            meals_section = single_menu.find('pre')

            if meals_section is not None:
                meals = meals_section.get_text().split('\r\n')

                menus['alacarte']['status'] = 'AVAILABLE'

                if len(meals) > 0:
                    for meal in meals:
                        if meal:
                            menus['alacarte']['menu'].append({
                                'title': to_title(meal),
                            })
        elif single_menu.find('h3').text == 'Sosyal Bina ve Faculty Club':
            # social building
            meals_section = single_menu.find('pre')

            if meals_section is not None:
                meals = meals_section.get_text().split('\r\n')

                menus['social_building']['status'] = 'AVAILABLE'

                if len(meals) > 0:
                    for meal in meals:
                        if meal:
                            menus['social_building']['menu'].append({
                                'title': to_title(meal),
                            })

    # set statuses
    for menu_key in menus:
        menu = menus[menu_key]

        if (len(menu.get('menu'))) != 0:
            menu['status'] = 'AVAILABLE'
        else:
            menu['status'] = 'UNAVAILABLE'

    return menus
