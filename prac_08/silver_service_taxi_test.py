"""
CP1404/CP5632 Practical
Test Silver Service Taxi
"""
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    # Create a new fancy taxi
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 1.5)

    # Drive the taxi 40km
    fancy_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(fancy_taxi)
    print("Current fare: $ {:.2f}".format(fancy_taxi.get_fare()))


if __name__ == '__main__':
    main()