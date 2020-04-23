"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from prac_06.programming_languages import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", False, 1995)
    cpp = ProgrammingLanguage("C++", "Static", False, 1983)

    languages = [ruby, python, visual_basic, java, cpp]
    print(ruby)
    print(python)
    print(visual_basic)
    print(java)
    print(cpp)
    print("Dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()