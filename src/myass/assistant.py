import oaix

import myass.config


class Assistant:
    def __init__(self, name):
        self.config = myass.config.Configuration(name)
        self.api = oaix.Api()

    def __call__(self, content=None, messages=None):
        params = self.config.flatten()
        try:
            params['model']
        except KeyError:
            params['model'] = 'gpt-3.5-turbo'
        if messages is not None:
            params['messages'].extend(messages)
        if content is not None:
            params['messages'].append({'role': 'user', 'content': content})
        r = self.api.post('chat/completions', json=params)
        for choice in r['choices']:
            yield choice['message']['content']
