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

    try:
        menu = fetch('2016-05-19')
    except:
        ...


License
-------

Copyright (c) 2016 H.Gökhan Sarı

Licensed under the MIT License.