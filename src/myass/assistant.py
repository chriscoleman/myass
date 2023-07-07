import copy

import oaix

import myass.config


class Assistant:
    def __init__(self, name):
        self.config = myass.config.Config(name)
        self.api = oaix.Api()
        self.messages = []

    def __call__(self, content=None, messages=None):
        params = copy.deepcopy(self.config.flatten())
        if messages is not None:
            self.messages.extend(messages)
        if content is not None:
            self.messages.append({'role': 'user', 'content': content})
        params['messages'].extend(self.messages)
        r = self.api.post('chat/completions', json=params)
        for choice in r['choices']:
            yield choice['message']['content']
            self.messages.append(choice['message'])
