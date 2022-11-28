import math


def calculate_ab(a, b, c):
    if c == 's':
        return a + b
    elif c == 'd':
        return a - b
    elif c == 'p':
        return a * b
    elif c == 'q':
        return a / b
    elif c == 'r':
        return a % b
    elif c == 'l':
        return math.log10(a)
    elif c == 'e':
        return a ** b
    else:
        return "not a valid option, try again."
