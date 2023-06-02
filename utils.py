import random


def id_generator():
    count = 0
    while True:
        count += 1
        yield count


def random_color():
    colors = ['red', 'green', 'blue', 'aqua']
    while True:
        random.shuffle(colors)
        for color in colors:
            yield color


random_colors = random_color()

id_gen = id_generator()
