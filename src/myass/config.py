import os

import confuse


class Configuration(confuse.Configuration):
    def __init__(self, name):
        super().__init__('assistants')

        filename = os.path.join(self.config_dir(), name)
        if not filename.endswith('.yaml'):
            filename += '.yaml'
        self.set_file(filename)
