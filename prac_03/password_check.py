MIN_LENGTH = 4
MAX_LENGTH = 10


def main():
    password = get_password()
    password_to_asterisks(password)


def get_password():
    password = input("Enter password here: ")
    while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        print("password must be {} to {} characters".format(MIN_LENGTH, MAX_LENGTH))
        password = input("Enter password here: ")
    return password


def password_to_asterisks(password):
    for character in password:
        print("*", end=' ')


main()