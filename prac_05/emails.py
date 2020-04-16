"""
CP1404/CP5632 Practical
Email to name dictionary
"""


def main():
    email_to_name = {}
    email = input("Enter your email: ")
    while email != "":
        name = get_name(email)
        confirm = input("Verify that your name is {} (Y/n): ".format(name))
        if confirm.upper() != "Y" and confirm == "":
            name = input("Enter your name: ")
        email_to_name[email] = name
        email = input("Enter your email: ")

    for email, name in email_to_name.items():
        print ("{} ({})".format(name, email))


def get_name(email):
    username = email.split('@')[0]
    period = username.split('.')
    name = " ".join(period).title()
    return name


main()