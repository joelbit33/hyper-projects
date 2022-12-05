def check_number(num):
    sentence = ''

    if num % 2 == 0:
        sentence += f'{num} is even, and'
    else:
        sentence += f'{num} is not even, and'

    if num > 1:
        is_prime = None
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
                break
    else:
        return "not an option!"

    if is_prime:
        sentence += f' {num} is a prime.'
    else:
        sentence += f' {num} is a non-prime.'
    return sentence


print(check_number(-4))
