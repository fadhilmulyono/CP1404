import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print(random.randint(1, 100))  # produce a random number between 1 and 100 inclusive

'''
Answers to questions 1-3:

What did you see on line 1? A whole number
What was the smallest number you could have seen, what was the largest?
Smallest number = 5
Largest number = 20

What did you see on line 2? A whole odd number
What was the smallest number you could have seen, what was the largest?
Smallest number = 3
Largest number = 9
Could line 2 have produced a 4? No

What did you see on line 3? A decimal number with 15 decimal places
What was the smallest number you could have seen, what was the largest?
Smallest number = 2.5
Largest number = 5.5
'''