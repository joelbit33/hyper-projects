def sum_admission(age_list):
    total_sum = 0
    if not age_list:
        return False
    else:
        for i in age_list:
            if i <= 2:
                pass
            elif i > 2 and i < 12:
                total_sum += 14.00
            elif i >= 65:
                total_sum += 18.00
            else:
                total_sum += 23.00
    return total_sum


age_list = []
user_count = 1

while True:
    user_input = input(f"Input age of person.{user_count}: ")
    if user_input == "":
        break
    else:
        age_list.append(int(user_input))
        user_count += 1

total_sum = sum_admission(age_list)
print(total_sum)
