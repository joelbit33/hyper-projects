"""Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using the Pythagorean
theorem, as the functions result. Include inputs that read the lengths of
the shorter sides of a right triangle from the user, use your function to compute the
length of the hypotenuse, and display the result."""
import math


def calculate_hypotenuse(a, b):
    c = math.sqrt((a**2) + (b**2))
    return round(c, 2)


def print_triangle():
    print('    /|')
    print('   / |')
    print('  /  |a')
    print(' /   |')
    print('/    |')
    print('-----')
    print('   b')


print_triangle()
while True:
    a = input("Enter length of side a: ")
    b = input("Enter length of side b: ")
    if a.isnumeric() and b.isnumeric():
        c = calculate_hypotenuse(int(a), int(b))
        break
    else:
        print('Not numeric values.')
        continue
print(c)
