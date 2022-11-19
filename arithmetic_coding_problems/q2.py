def convert_fuel_effiency(mpg):
    l_per_100km = round(235.21 / mpg, 3)
    return l_per_100km


user_mpg = float(input("enter MPG: "))
user_mpg_converted = convert_fuel_effiency(user_mpg)
print(f"{user_mpg} miles per gallon is: {user_mpg_converted} liters per hundred km")
