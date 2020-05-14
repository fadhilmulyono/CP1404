"""
Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).

Create a text file called numbers.txt and save it in your prac_02 directory.
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
which should be... 59.

Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
"""

NAME_FILE = "name.txt"
NUMBER_FILE = "number.txt"

# Quick Program 1
out_file = open(NAME_FILE, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# Quick Program 2
in_file = open(NAME_FILE, 'r')
name = in_file.read()
in_file.close()
print("Your name is " + name)

# Quick Program 3
in_file = open(NUMBER_FILE, 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
result = number1 + number2
in_file.close()
print("Sum of 2 numbers = {0}".format(str(result)))

# Quick Program 4
in_file = open(NUMBER_FILE, 'r')
number3 = int(in_file.readline())
total = 0
Lines = in_file.readlines()
for line in Lines:
    print(line.strip())
    total = number1 + number2 + number3
in_file.close()
print("Sum of 3 numbers = {0}".format(str(total)))