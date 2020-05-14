"""CP1404/CP5632 Practical -  Guitars."""
CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, reference name for guitar
        year: integer, the year when the guitar was made
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return "{} ({}) : ${})".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of the guitar, which is the current year minus the year the guitar was made."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return whether the guitar is vintage or not, if more than 50 years old."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort guitars by year released"""
        return self.year < other.year