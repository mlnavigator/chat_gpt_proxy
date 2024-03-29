from openai import OpenAI


def get_model(api_key):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )

    return client


def chat_response(messages, client, model_name='gpt-3.5-turbo', max_tokens=1000, temperature=None,):
    try:
        if temperature is None:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model_name,
                max_tokens=max_tokens,
            )
        else:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model_name,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        return True, chat_completion.choices[0].message.content
    except Exception as e:
        return False, f'Error. {str(e)}'
