from random import randint

att = [
    ('red', '\033[31m'),
    ('green', '\033[32m'),
    ('orange', '\033[33m'),
    ('blue', '\033[34m'),
    ('purple', '\033[35m'),
    ('cyan', '\033[36m'),
    ('lightgrey', '\033[37m'),
    ('darkgrey', '\033[90m'),
    ('lightred', '\033[91m'),
    ('lightgreen', '\033[92m'),
    ('yellow', '\033[93m'),
    ('lightblue', '\033[94m'),
    ('pink', '\033[95m'),
    ('lightcyan', '\033[96m'),
    ('reset', '\033[0m')
]


def colored(string):
    return (f'{get_random_color()}{string}{get_reset()}')


def get_color(color):
    return att[color]


def get_random_color():
    x = randint(0, 13)
    return f'{att[x][1]}'


def get_reset():
    return att[14][1]
