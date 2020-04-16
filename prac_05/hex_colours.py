"""
CP1404/CP5632 Practical
Hexadecimal colours lookup
"""

HEX_COLOURS = {'blue': '#0000FF',
               'purple': '#800080',
               'violet': '#EE82EE',
               'indigo': '#4B0082',
               'pink': '#FFC0CB',
               'red': '#FF0000',
               'orange': '#FFA500',
               'mustard': '#FFDB58',
               'brown': '#A52A2A',
               'yellow': '#FFFF00',
               'olive': '#808000',
               'green': '#008000',
               'aqua': '#00FFFF',
               'light blue': '#ADD8E6',
               'white': '#FFFFFF',
               'blue-gray': '#6699CC',
               'charcoal': '#36454F',
               'black': '#000000'}
# print(HEX_COLOURS)

color = input("Enter a colour name: ").lower()
while color != "":
    if color in HEX_COLOURS:
        print("The colour {} has the hexadecimal code {}".format(color, HEX_COLOURS.get(color)))
    else:
        print("Invalid colour")
    color = input("Enter a colour name: ").lower()
