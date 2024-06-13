from openai import OpenAI


def get_model(api_key):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )

    return client


def chat_response(messages, client, model_name='gpt-3.5-turbo', max_tokens=1000, temperature=None, **kwargs) -> (
        tuple)[bool, dict]:
    try:
        if temperature is None:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model_name,
                max_tokens=max_tokens,
                **kwargs
            )
        else:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model_name,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
        res = chat_completion.dict()
        res['text'] = chat_completion.choices[0].message.content
        return True, res
    except Exception as e:
        return False, {'text': f'Error. {str(e)}'}
