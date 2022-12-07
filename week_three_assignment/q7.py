def calc_shipping_fee(item_amount):
    total_cost = 10.95
    for i in range(1, item_amount):
        total_cost += 2.95
    return f'Total shipping fee is ${round(total_cost, 2)}'


user_input = int(input("Enter amount of items: "))
total_amount = calc_shipping_fee(user_input)
print(total_amount)
