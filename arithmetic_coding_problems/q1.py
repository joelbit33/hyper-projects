from q1_module import calculate_ab


def main():
    active = True
    latest_answers = []

    while active:
        try:
            number_a = int(input("Enter first number: "))
            number_b = int(input("Enter second number: "))
        except ValueError:
            print("Not a valid number")
            continue
        else:

            print("\n(s)um\n(d)ifference\n(p)roduct\n(q)uotient\n(r)emainder\n(l)ogarithm of a base 10\n(e)xponentiate")
            print("\n--(q) to quit:")

            arithmetic_choice = input("")

            if arithmetic_choice == 'q':
                break
            else:
                answer = calculate_ab(number_a, number_b, arithmetic_choice)
                latest_answers.append(answer)
                print(answer)
                print(latest_answers)


if __name__ == "__main__":
    main()
