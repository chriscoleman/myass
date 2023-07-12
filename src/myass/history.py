import readline

import redis


class History:
    def __init__(self, namespace, n=1000):
        self.namespace = namespace
        self.n = n
        self.redis = redis.Redis(decode_responses=True)

    def __enter__(self):
        self.backup = [readline.get_history_item(i+1)
                       for i in range(readline.get_current_history_length())]
        readline.clear_history()
        for item in self.redis.lrange(self.key, -self.n, -1):
            readline.add_history(item)
        self.redis.expire(self.key, 86400)

    def __exit__(self, *args):
        for i in range(readline.get_current_history_length()):
            self.redis.rpush(self.key, readline.get_history_item(i+1))
        self.redis.expire(self.key, 86400)
        readline.clear_history()
        for item in self.backup:
            readline.add_history(item)

    @property
    def key(self):
        return ':'.join((__name__, self.namespace))
