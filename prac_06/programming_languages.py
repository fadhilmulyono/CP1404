"""CP1404/CP5632 Practical - Programming Languages."""


class ProgrammingLanguage:
    """Represent a Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

        name: string, reference name for programming language
        typing: string, a logical system comprising a set of rules that assigns a property called a type to the various
        constructs of a computer program
        reflection: string, he ability for a program to determine various pieces of information about an object at
        run-time
        year: integer, the year when the programming language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Return if the programming language is dynamically typed"""
        return self.typing == "Dynamic"


def run_tests():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(ruby)
    print(python)
    print(visual_basic)
    print("Dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()