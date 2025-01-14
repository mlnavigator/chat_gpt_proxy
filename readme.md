## Как работает сервис

Сервис работает в виде API - отправьте POST запрос на end_point /chat_complete

### формат запроса json 

- кидаем только одно сообщение (промпт) вида {'prompt': 'Привет, какая ты версия модели?'}
  в этомм случае нужно только поле 'prompt'

- кидаем историю переписки вида {'messages': [list of messages]}. В этом случае нужно только поле 'messages':

``` 
{'messages': [  
    {"role": "system", "content": "You are a helpful assistant."},  
    {"role": "user", "content": "Who won the world series in 2020?"},  
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},  
    {"role": "user", "content": "Where was it played?"}  
  ]}
```



### Пример кода на python3 для работы с сервисом

```

import requests

data = {'prompt': 'Привет, какая ты версия модели?'}

```


если необходимо изменить параметры генерации,

то можно добавить в запрос поле 'generate_params', например:

```  
data = {'prompt': 'Привет, Медвед! Расскажи что ты вчера видел?',  
        'generate_params': {  
               'model_name': 'gpt-4o',  
               'max_tokens': 3000,  
               'temperature': 0.8  
              }  
        }  
```

Если generate_params не задавать, или задавать частично,

то для не указанных параметров будут использоваться умолчания:

- model_name: str = 'gpt-4o-mini'
- temperature: None|float = None

Устанавливайте параметры для generate_params согласно актуальной документации OpenAI - примеры параметров ниже могут быть устаревшими и показывают общий смысл работы с прокси.

Установите свой access_token в параметрах окружения перед запуском приложения,

иначе будет использоваться токен по умолчанию '123456'

#### Обязательно установите свой openai_token в заголовке запроса
Токен Open_ai нигде не сохраняется и используется только в рамках одного запроса

```python3

headers = {'access-token': '123456',  
           'openai-token': 'your OpenAi api key'}  
           
#### url='http://localhost:9081/chat_complete' - замените на ваш актуальный адрес сервера  

r = requests.post(url='http://localhost:9081/chat_complete', json=data, headers=headers)  

print(r.status_code)

>>> 200

print(r.json())

>>> {'text': 'Привет! Я являюсь версией последней модели, и постоянно обновляюсь, чтобы быть самой современной и эффективной. Как я могу помочь тебе сегодня?', 'status': 'ok'}

```

Например
```
headers = {'access-token': access-token,
           'openai-token': token} 
data = {
            "prompt": prompt  # или 'messages': messages
        }

data['generate_params'] = { 
            'model_name': model_name, 
            'max_tokens': max_tokens, 
            'temperature': temperature,
            # другие параметры какие нужны для передачи в опен аи, они все будут проброшены
}
api_url='https://chatgpt-proxy.mlnavigator.ru/chat_complete'
r = requests.post(url=api_url, json=data, headers=headers)

# r.json() содержит не только ключ text с ответом, но и все что вернуло апи чат гпт, смотрите актуальные ключи в ответа
```


## Установка прокси сервиса

Исходник сервиса
- https://github.com/mlnavigator/chat_gpt_proxy

Если токен доступа не меняли, то по умолчанию он 'access-token': '123456'

можете в скрипте rebuild.sh поменять токен доступа


Для работы требуется docker

```commandline

git clone https://github.com/mlnavigator/chat_gpt_proxy.git

cd 'folder_with_project'

/bin/bash ./rebuild.sh
```

Если хотите чтобы трафик был шифрованный, то установите nginx и в нем настройте самоподписанные сертификаты

По умолчанию сервис будет доступен по адресу Ваш_IP_адрес_сервера:9081

