"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAME = {'QLD': "Queensland",
              'NSW': "New South Wales",
              'NT': "Northern Territory",
              'WA': "Western Australia",
              'SA': 'South Australia',
              'ACT': "Australian Capital Territory",
              'VIC': "Victoria",
              'TAS': "Tasmania"}
# print(STATE_NAME)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAME:
        print(state, "is", STATE_NAME[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
