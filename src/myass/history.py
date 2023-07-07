import atexit
import os
import readline

import appdirs


def initialize(appname='myass', filename='history'):
    data_dir = appdirs.user_data_dir(appname)
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    histfile = os.path.join(data_dir, filename)
    try:
        readline.read_history_file(histfile)
    except FileNotFoundError:
        pass
    atexit.register(readline.write_history_file, histfile)
