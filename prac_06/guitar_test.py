"""CP1404/CP5632 Practical - Client code to use the Guitar class."""

from prac_06.guitar import Guitar
CURRENT_YEAR = 2020


def run_tests():
    name = "Gibson L-5 CES"
    cost = 16035.40
    year = 1922

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2010, 1512.9)
    jcu = Guitar("50-year old", 1970, 2003.15)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 10, other.get_age()))
    print("")
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(jcu.name, False, jcu.is_vintage()))


if __name__ == '__main__':
    run_tests()