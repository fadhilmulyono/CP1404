def main():
    # 1. Basic list operations
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)

    print("First number: {}". format(numbers[0]))
    print("Last number: {}".format(numbers[4]))
    print("Smallest number: {}".format(min(numbers)))
    print("Largest number: {}".format(max(numbers)))
    print("Average of {} numbers: {}".format(len(numbers), sum(numbers)/len(numbers)))

    # 2. Woefully inadequate security checker

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    login = input("Enter your Login ID: ")
    if login in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()

"""
Number: 5
Number: 20
Number: 1
Number: 2
Number: 3
The first number is 5
The last number is 3
The smallest number is 1
The largest number is 20
The average of the numbers is 6.2
"""