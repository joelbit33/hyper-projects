"""An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item, and $2.95 for each subsequent item. Write a function that takes the
number of items in the order as its only parameter. Return the shipping charge for
the order as the functions result. Include user inputs that read the number of
items purchased from the user and display the shipping charge."""


def calc_shipping_fee(item_amount):
    total_cost = 10.95
    for i in range(1, item_amount):
        total_cost += 2.95
    return f'Total shipping fee is ${round(total_cost, 2)}'


user_input = int(input("Enter amount of items: "))
total_amount = calc_shipping_fee(user_input)
print(total_amount)
