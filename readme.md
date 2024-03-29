## Установка прокси сервиса

```commandline

git clone https://github.com/mlnavigator/chat_gpt_proxy.git

cd 'folder_with_project'

/bin/bash ./rebuild.sh
```
можете в скрипте rebuild.sh поменять токен доступа

Если хотите чтобы трафик был шифрованный, то установите nginx и в нем настройте самоподписанные сертификаты

По умолчанию сервис будет доступен по адресу Ваш_IP_адрес_сервера:9081


## Как работает сервис

Сервис работает в виде API - отправьте POST запрос на end_point /chat_complete

формат запроса json вида {'prompt': 'Привет, какая ты версия модели?'}

Далее пример кода на python3 для работы с сервисом

```

import requests

data = {'prompt': 'Привет, какая ты версия модели?'}

```


если необходимо изменить параметры генерации,

то можно добавить в запрос поле 'generate_params', например:

```
data = {'prompt': 'Привет, Медвед! Расскажи что ты вчера видел?',
        'generate_params': {
               'model_name': 'gpt-4-0125-preview',
               'max_tokens': 3000,
               'temperature': 0.8
              }
        }
```

Если generate_params не задавать, или задавать частично,

то для не указанных параметров будут использоваться умолчания:

- model_name: str = 'gpt-3.5-turbo'
- max_tokens: int = 1000
- temperature: None|float = None


Установите свой access_token в параметрах окружения перед запуском приложения,

иначе будет использоваться токен по умолчанию '123456'

#### Обязательно установите свой openai_token в заголовке запроса
Токен Open_ai нигде не сохраняется и используется только в рамках одного запроса

```

headers = {'access_token': '123456',
           'openai_token': 'your OpenAi api key'}
           
#### url='http://localhost:9081/chat_complete' - замените на ваш актуальный адрес сервера

r = requests.post(url='http://localhost:9081/chat_complete', json=data, headers=headers)

print(r.status_code)

>>> 200

print(r.json())

>>> {'text': 'Привет! Я являюсь версией последней модели, и постоянно обновляюсь, чтобы быть самой современной и эффективной. Как я могу помочь тебе сегодня?', 'status': 'ok'}

```
