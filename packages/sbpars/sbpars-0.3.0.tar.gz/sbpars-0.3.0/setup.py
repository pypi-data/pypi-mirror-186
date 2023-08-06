# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sbpars', 'sbpars.scripts']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'flake8>=6.0.0,<7.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.5.2,<2.0.0']

entry_points = \
{'console_scripts': ['sbpars = sbpars.scripts.sbpars:main']}

setup_kwargs = {
    'name': 'sbpars',
    'version': '0.3.0',
    'description': '',
    'long_description': '## sbpars - simply bank ordering parser\n\n### Что это?\n\nЭто простой парсер в форматы .csv и .xlsx для данных, выгружаемых из истории операций по карте одного банка. Написано и предназначено для личного использования: я веду учёт личных финансов в таблице и устал забивать руками каждый платёж по карте.\n\nПрограмма не производит никаких взаимодействий с сайтом банка и личным кабинетом клиента по сети, не использует чужие данные и вообще не даёт доступа ни к чему такому, к чему изначально нет доступа у пользователя. Функционал программы ограничен предоставлением данных, изначально доступных пользователю, в удобной форме таблицы.\n\n### Как использовать?\n\nЗаходим в личный кабинет в историю операций по карте. Кликаем на кнопку "Отчёт по карте". Настраиваем период, за который нужна выгрузка. Сохраняем страницу средствами браузера.\n\nОткрываем консоль, заходим в папку сохраненной страницы с окончанием "_files". Приложению для работы нужен файл index.html, он находится в данной папке.\n\nДалее два варианта: можно установить утилиту через pip, можно работать с исходным кодом.\n\n*Вариант 1*\n\nУстанавливаем и запускаем в папке, где находится index.html:\n```\npip install sbpars\nsbpars\n```\n\n*Вариант 2*\n\nКопируем index.html в папку со скриптом и запускаем\n\n```\npip install poetry\nmake start\n```\n\nЕсли всё прошло успешно, то в этой же папке появятся файлы transactions с расширениями .csv и .xlsx со списком транзакций\n',
    'author': 'qmka',
    'author_email': 'eidolonzx@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
