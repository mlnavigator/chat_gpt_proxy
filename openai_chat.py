from openai import OpenAI


def get_model(api_key):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )

    return client


def chat_response(messages, client, model_name='gpt-4o-mini', temperature=None, **kwargs) -> (
        tuple)[bool, dict]:
    try:
        if temperature is None:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model_name,
                **kwargs
            )
        else:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model_name,
                temperature=temperature,
                **kwargs
            )
        res = chat_completion.dict()
        res['text'] = chat_completion.choices[0].message.content
        return True, res
    except Exception as e:

        try:
            try:
                data_to_return = res
            except:
                data_to_return = chat_completion
        except:
            data_to_return = {}

        return False, {'text': f'Error. {str(e)}\n\n{data_to_return}\n'}
