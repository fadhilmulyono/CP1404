"""CP1404/CP5632 Practical - Tests to actually play the guitars for the Guitar class."""

from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitar collection")
    print("Add at least one to the collection.")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "was added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("My guitar collection")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(This is a vintage guitar!)"
            print("Guitar {0}: {1.name:>10} ({1.year}), worth ${1.cost:5,.2f} {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars. Please buy one right now!")


main()