
def compute_avarage(number_list):
    total_amount = 0
    for i in number_list:
        total_amount += i
    avarage_count = round(total_amount / len(number_list), 2)
    return avarage_count


number_list = []
current_number = 1

while True:
    user_input = input(f'Enter number.{current_number}: ')

    if user_input.isnumeric():
        if user_input != "0":
            number_list.append(float(user_input))
            current_number += 1
        elif user_input == "0" and len(number_list) == 0:
            print("You can't enter 0 as the first number")
        else:
            break
    else:
        print("Not a number")


avarage_amount = compute_avarage(number_list)

print(avarage_amount)
