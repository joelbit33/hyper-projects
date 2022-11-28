# A PROGRAM THAT SETS UP A USER ACCOUNT
#


def create_account():
    print("Hello there, create your account!")
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    return new_username, new_password


def update_user_database(new_username, new_password):
    user_database['username'] = new_username
    user_database['password'] = new_password
    print(f'Welcome {username}, you can now log in')


def log_in():
    print("Log in")
    prompt_user


def check_username():
    pass


def check_password():
    pass


def greet_user():
    pass


user_database = {}

new_username, new_password = create_account()
update_user_database(new_username, new_password)

is_logged_in = log_in()
