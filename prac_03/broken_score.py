"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


# Fix this!

def main():
    score = float(input("Enter score: "))
    get_score(score)
    get_random_score()


def get_score(score):
    if (score < 0) or (score > 100):
        result = "Invalid score"
    elif (score >= 50) and (score < 90):
        result = "Passable"
    elif (score >= 90) and (score <= 100):
        result = "Excellent"
    elif score < 50:
        result = "Bad"
    print(result)


def get_random_score():
    score = random.randint(0, 100)
    print("Random score: " + str(score))
    get_score(score)


main()
