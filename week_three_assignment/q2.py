# The following program is used to find out the roots of the quadratic equation

import math


def equationroots(x, y, z):

    discri = y * y - 4 * x * z

    sqrt_val = math.sqrt(abs(discri))

    # checking condition for discriminant

    if discri > 0:

        print(" real and different roots ")

        print((-y + sqrt_val)/(2 * x))

        print((-y - sqrt_val)/(2 * x))

    elif discri == 0:

        print(" real and same roots")

        print(-y / (2 * x))

    # when discriminant is less than 0

    else:

        print("Complex Roots")

        print(- y / (2 * x), " + i", sqrt_val)

        print(- y / (2 * x), " - i", sqrt_val)


# Driver Program
x = 1

y = 10

z = -24


if x == 0:

    print("Input correct quadratic equation")


else:

    equationroots(x, y, z)
