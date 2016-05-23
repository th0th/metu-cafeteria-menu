===================
metu-cafeteria-menu
===================

``metu-cafeteria-menu`` is a utility for fetching **Middle East Technical University**'s cafeteria menu. It gets data from cafeteria's website and parses it.

Install
-------

.. code-block:: sh

    pip install metu-cafeteria-menu

Usage
-----

.. code-block:: python

    from metu_cafeteria_menu import fetch
    from metu_cafeteria_menu.exceptions import DateException, RequestException

    try:
        menu = fetch('2016-05-19')
    except RequestException as e:
        # something went wrong while trying to connect to cafeteria website
        print(str(e))
    except DateException as e:
        # menu is not available for the selected date, it may be weekend or holiday
        print(str(e))


License
-------

Copyright (c) 2016 H.Gökhan Sarı

Licensed under the MIT License.