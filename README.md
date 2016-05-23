# metu-cafeteria-menu

Fetches **Middle East Technical University** cafeteria's menu from its website.

## Install

```sh
pip install metu-cafeteria-menu
```

## Usage

```py
from metu_cafeteria_menu import fetch

try:
    menu = fetch('2016-05-19')
except:
    ...
```

## License

Copyright (c) 2016 H.Gökhan Sarı

Licensed under the MIT License.