import math


def calculate_polygon_area(s, n):

    return (n * s**2) / (4 * math.tan(math.pi / n))


side_length = float(input("Enter side length of polygon in m: "))
side_amount = int(input("Enter amount of sides of polygon: "))

area = calculate_polygon_area(side_length, side_amount)

print(f"The area is: {area} square meter")
