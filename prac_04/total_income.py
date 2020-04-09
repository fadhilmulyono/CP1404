"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    income_per_month = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        income_per_month.append(income)

    print_report(income_per_month)


def print_report(income_per_month):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(income_per_month):
        total += income
        print("Month {} - Income: ${:.2f} Total: ${:.2f}".format(month + 1, income, total))


main()
