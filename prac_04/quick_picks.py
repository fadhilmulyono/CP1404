import random

NUMS_PER_DRAW = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    print("Enter your number of Quick Pick(s) for the Gold Lotto lottery,")
    print("which uses {} numbers ranged from {} to {}.".format(NUMS_PER_DRAW, MIN_NUMBER, MAX_NUMBER))
    quick_picks = int(input("Number of Quick Picks: "))
    while quick_picks < 1:
        print("No sense to pick zero or negative numbers of Quick Picks!")
        quick_picks = int(input("Number of Quick Picks: "))
    print("Your chance of matching all numbers with this combination is {} in 8,145,060.".format(quick_picks))
    print("\n")
    print("Here are your {} lottery tickets: ".format(quick_picks))
    for i in range(quick_picks):
        quick_pick = []
        for j in range(NUMS_PER_DRAW):
            numbers = random.randint(MIN_NUMBER, MAX_NUMBER)
            while numbers in quick_pick:
                numbers = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(numbers)
        quick_pick.sort()
        print("-".join("{:2}".format(number) for number in quick_pick))


main()

"""
How many quick picks? 5
 1 12 14 15 30 36
 2  5  8 33 38 41
 2 12 19 22 29 43
13 21 28 29 42 43
 3  4 10 11 32 44
"""