MIN_LENGTH = 4


def main():
    password = get_password(MIN_LENGTH)
    get_asterisks(password)


def get_password(MIN_LENGTH):
    print("Please enter your password.")
    print("Your password must be at least {} characters.".format(MIN_LENGTH))
    password = input("> ")
    while MIN_LENGTH > len(password):
        print("Invalid password!")
        password = input("> ")
    print("Password accepted")
    return password


def get_asterisks(sequence):
    print("*" * len(sequence))


main()
