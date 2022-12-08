def sum_sub(num_item):
    base_cost = 10.95
    if num_item == 1:
        return base_cost
    elif num_item > 1:
        return base_cost + (2.95 * (num_item - 1))


def print_shipping_cost(total_sum):
    print(f"Your total shipping cost is ${total_sum}.")
    print("--------------------------")


def get_items():
    while True:
        num_item = int(input("How many items to ship: "))
        total_sum = sum_sub(num_item)
        print_shipping_cost(total_sum)


get_items()
