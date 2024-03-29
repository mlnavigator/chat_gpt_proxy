import os
import json
import markdown
from bottle import get, post, run, request, response

from openai_chat import get_model, chat_response

access_key = os.getenv('ACCESS_KEY')
if access_key is None:
    access_key = '123456'

@get('/')
@get('/chat_complete')
def chat_complete_get():
    with open(os.path.join(os.path.dirname(__file__),'readme.md'), 'r') as fd:
        data = fd.read()
    return markdown.markdown(data)


@post('/chat_complete')
def chat_complete():
    try:
        access_token = request.get_header('access-token')
        if access_token != access_key:
            response.status = 403
            return json.dumps({'text': 'Доступ запрещен, токен не верный', 'status': 'error'}, ensure_ascii=False)

        api_token = request.get_header('openai-token')

        request_data = request.json
        prompt = request_data['prompt']
        params = request_data.get('generate_params', None)
        params = params if params else dict()

        openai_client = get_model(api_token)
        # print('api_token', api_token)
        # print('prompt', prompt)
        # print('params', params)
        status, text = chat_response(prompt, openai_client, **params)

        if status:
            response.status = 200
            return json.dumps({'text': text, 'status': 'ok'}, ensure_ascii=False)
        else:
            response.status = 502
            return json.dumps({'text': text, 'status': 'error'}, ensure_ascii=False)
    except Exception as e:
        response.status = 500
        return json.dumps({'text': f'Error. {str(e)}', 'status': 'error'}, ensure_ascii=False)


if __name__ == '__main__':
    # run(host='localhost', port=9081)
    run(host='0.0.0.0', port=9081, server='gunicorn', reload=True, workers=4, debug=True)
