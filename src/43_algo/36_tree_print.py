import math


def tree(levels=5):
    total_odd_levels = (levels * 2) - 1
    counter = 0
    spacing = math.ceil(total_odd_levels / 2)
    spacing_counter = 0

    while counter <= total_odd_levels:
        if counter % 2 == 0:
            counter += 1
            continue

        spacing_chars = " " * (spacing - spacing_counter)
        star_chars = "*" * counter

        print(spacing_chars + star_chars)
        counter += 1
        spacing_counter += 1


def box(width=10, height=10):
    for h in range(0, height):
        if h == 0:
            print("*" * width)
        elif h == (height - 1):
            print("*" * width)
        else:
            char = "*" + (" " * (width - 2)) + "*"
            print(char)


tree(10)
box(25, 10)
