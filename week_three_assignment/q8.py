"""8. In this exercise, you will write a function that determines whether or not a password
is good. We will define a good password to be one that is at least 8 characters
long and contains at least one uppercase letter, at least one lowercase letter, and at
least one number. Your function should return true if the password passed to it as
its only parameter is good. Otherwise, it should return false."""


def check_secure_password(password):
    check_count = 0
    char_list = list(password)

    if len(char_list) < 8:
        return False
    else:
        check_count += 1

    for i in char_list:
        if i.isupper():
            check_count += 1
            break
    for i in char_list:
        if i.islower():
            check_count += 1
            break
    for i in char_list:
        if i.isnumeric():
            check_count += 1
            break

    if check_count == 4:
        return True
    else:
        return False


user_password = input("Enter a strong password: ")
is_secure = check_secure_password(user_password)

print(is_secure)
