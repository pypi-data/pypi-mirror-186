# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['yandexid',
 'yandexid.errors',
 'yandexid.schemas',
 'yandexid.yandexid',
 'yandexid.yandexoauth']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.3,<0.24.0', 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'yandexid',
    'version': '0.2.0',
    'description': 'Yandex ID oauth API wrapper',
    'long_description': '# Яндекс ID (OAuth) API\nБиблиотека для работы с API Яндекс ID (OAuth) для Python 3.10+.\nПоддерживает асинхронную работу.\n\n[Документация API](https://yandex.ru/dev/id/doc/dg/index.html)\n\n## Установка\n\n1. С помощью pip:\n    \n    ```bash\n    pip install yandexid\n    ```\n\n2. С помощью pip+git:\n    \n    ```bash\n    pip install https://github.com/LulzLoL231/yandexid.git\n    ```\n\n3. Из исходников:\n\n    ```bash\n    git clone https://github.com/LulzLoL231/yandexid\n    pip install ./yandexid\n    ```\n\n## Пример использования\n\n1. Получение OAuth токена:\n\n    ```python\n    from yandexid import YandexOAuth\n\n    yandex_oauth = YandexOAuth(\n        client_id=\'<client_id>\',\n        client_secret=\'<client_secret>\',\n        redirect_uri=\'<redirect_uri>\'\n    )\n    auth_url = yandex_oauth.get_authorization_url()\n    # Тут нужно перейти по ссылке auth_url и получить код авторизации\n    token = yandex_oauth.get_token_from_code(\'<code>\')\n    ```\n    Возвращает объект `Token` с информацией о OAuth токене. Формат объекта совпадает с [форматом ответа из API Яндекс ID](https://yandex.ru/dev/id/doc/dg/oauth/reference/console-client.html#console-client__token-body-title).\n\n\n2. Получение информации о пользователе:\n\n    ```python\n    from yandexid import YandexID\n\n    yandex_id = YandexID(\'<oauth_token>\')\n    user_info = yandex_id.get_user_info_json()\n    ```\n    Возвращает объект `User` с информацией о пользователе. Формат объекта совпадает с [форматом ответа из API Яндекс ID](https://yandex.ru/dev/id/doc/dg/api-id/reference/response.html).\n\n## Асинхронная работа\nЧтобы использовать асинхронность, используйте классы `AsyncYandexOAuth` и `AsyncYandexID`:\n\n```python\nfrom yandexid import AsyncYandexID\n\nyandex_id = AsyncYandexID(\'<oauth_token>\')\nuser_info = await yandex_id.get_user_info_json()\n```\nНазвание методов полностью совпадает с названием синхронных методов, не забывайте использовать `await` перед вызовом асинхронных методов.\n\nЛоготипы Яндекс ID и название сервиса "Яндекс ID" принадлежат Яндексу.\n',
    'author': 'Maxim Mosin',
    'author_email': 'max@mosin.pw',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/LulzLoL231/yandexid',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
