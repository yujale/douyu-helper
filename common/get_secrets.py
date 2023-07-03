import os
from common.dirs import *


def get_secrets(item):
    return os.environ[item]


if __name__ == '__main__':
    print(get_secrets('COOKIES'))
