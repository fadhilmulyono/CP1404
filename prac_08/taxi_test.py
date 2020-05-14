"""
CP1404/CP5632 Practical
Test Taxi
"""
from prac_08.taxi import Taxi


def main():
    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    prius_taxi = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi 40km
    prius_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(prius_taxi)
    print("Current fare: $ {:.2f}".format(prius_taxi.get_fare()))

    # Restart the meter (start a new fare) and then drive the car 100km
    prius_taxi.start_fare()
    prius_taxi.add_fuel(40)
    prius_taxi.drive(100)

    # Print the details and the current fare
    print(prius_taxi)
    print("Current fare: $ {:.2f}".format(prius_taxi.get_fare()))


if __name__ == '__main__':
    main()