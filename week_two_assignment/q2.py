def calculate_mean(x, y, z):
    return round((x + y + z) / 3, 2)


number_one = int(input("Number one: "))
number_two = int(input("Number two: "))
number_three = int(input("Number three: "))

mean_result = calculate_mean(number_one, number_two, number_three)

print(mean_result)
