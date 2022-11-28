# Write a simple calculator ( addition and subtraction from two number from user).
# Add the answers to a list called "answer_history"
# Let the user have the ability to See their answer history, and if they want to: Delete all their history.

def add_two_numbers(a, b):
    return a + b


def subtract_two_numbers(a, b):
    return a - b


answer_history = []

while True:
    first_number = int(input("Write a random number here: "))
    second_number = int(input("Write another random number here: "))

    user_choice = input(
        "Do you want to (a)dd numbers, (s)ubtract numbers, (h)istory, (d)elete history, or (q)uit: ")

    if user_choice == "a":
        addition_answer = add_two_numbers(first_number, second_number)
        print(
            f"The result of first_number plus second_number is:{addition_answer}")
        answer_history.append(addition_answer)
    elif user_choice == "s":
        subtraction_answer = subtract_two_numbers(first_number, second_number)
        print(
            f"The result of first_number minus second_number is:{subtraction_answer}")
        answer_history.append(subtraction_answer)
    elif user_choice == "h":
        print(answer_history)
    elif user_choice == "d":
        answer_history.clear()
    elif user_choice == "q":
        break

    else:
        print("Sorry, don't understand that!")

print("The while loop broke.")
