import os

import confuse


class Config(confuse.LazyConfig):
    def __init__(self, name):
        super().__init__('assistants', __name__)

        filename = os.path.join(self.config_dir(), name)
        if not filename.endswith('.yaml'):
            filename += '.yaml'
        self.set_file(filename)
