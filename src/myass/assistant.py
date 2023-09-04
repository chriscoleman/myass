import copy
import json

import oaix

import myass.config


class Assistant:
    def __init__(self, name):
        self.config = myass.config.Config(name)
        self.api = oaix.Api()
        self.messages = []

    def __call__(self, content):
        params = copy.deepcopy(self.config.flatten())
        self.messages.append({'role': 'user', 'content': content})
        params['messages'].extend(self.messages)
        r = self.api.post('chat/completions', json=params)
        m = r['choices'][0]['message']
        while m.get('function_call') is not None:
            fn = m['function_call']['name']
            try:
                f = getattr(self, fn)
            except AttributeError:
                r = None
            else:
                r = f(**json.loads(m['function_call']['arguments']))
            params['messages'].append({'role': 'function',
                                       'name': fn, 'content': r})
            r = self.api.post('chat/completions', json=params)
            params['messages'].pop()
            m = r['choices'][0]['message']
        self.messages.append(m)
        return m['content']
