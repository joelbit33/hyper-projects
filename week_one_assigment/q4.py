

def convert_feet(c, x):
    if c == "i":
        return x * 12
    elif c == "y":
        return x / 3
    elif c == "m":
        return x * 0.0001894


user_input_in_feet = float(input("Measurement in feet:"))
user_choice = input("To (i)nches, (y)ards, or (m)iles? ")
feet_converted = convert_feet(user_choice, user_input_in_feet)
print(feet_converted)
