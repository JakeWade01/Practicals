def main():

    password = input("Please Enter Password: ")
    password_len = int(len(password))
    min_password_len = 7

    password_len = get_password(min_password_len, password_len)
    print_asterisks(password_len)


def get_password(min_password_len, password_len):
    while password_len < min_password_len:
        print("Password must be more than 7 characters")
        print()
        password = input("Please Enter Password: ")
        password_len = int(len(password))
    return password_len


def print_asterisks(password_len):
    print("Password is: ", end='')
    for i in range(0, password_len, 1):
        print("*", end='')


main()
