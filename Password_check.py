def main():
    password = get_password()
    print("Your password is all set! {}".format(len(password) * '*'))


def get_password():
    password = input("Please enter your password: ")
    return password


main()
