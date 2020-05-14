"""
CP1404/CP5632 Practical
Count word occurrences in a string
"""

word_count = {}
text = input("Write a message: ")
words = text.split()
# Get word frequency
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

# Sort words by alphabetical order
words = list(word_count.keys())
words.sort()

# Determine the longest word, then make spaces between words, colon, and number of occurrences
# Based on the length of the longest word
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))