"""
CP1404/CP5632 Practical
Taxi Simulator
"""
from prac_06.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """[C] hoose taxi
[D] rive
[Q] uit"""


def main():
    bills = 0
    taxis = [SilverServiceTaxi("Blue Bird", 100, 2), SilverServiceTaxi("Express", 100, 1.5), SilverServiceTaxi("Gamya", 100, 1.25),
             SilverServiceTaxi("Taxiku", 100, 1), Taxi("Prius", 100)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("\n")
            print("Choose a taxi:")
            display_taxis(taxis)
            taxi_choice = int(input(">> "))
            chosen_taxi = taxis[taxi_choice]
            print(chosen_taxi)
            print("\n")
        elif choice == "D":
            print("\n")
            chosen_taxi.start_fare()
            print("Enter driving distance (km):")
            distance = int(input(">> "))
            chosen_taxi.drive(distance)
            fare = chosen_taxi.get_fare()
            print("Your recent trip with {} costs you ${:.2f}.".format(chosen_taxi.name, fare))
            bills += fare
            print("\n")
        else:
            print("Invalid option")
            print("\n")
        print("Your current bills: ${:.2f}".format(bills))
        print(MENU)
        choice = input(">>> ").upper()
    print("\n")
    print("Your total trip cost today: ${:.2f}".format(bills))
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def run_tests():
    """Run tests to show workings of Car and Taxi classes."""
    test_bus = Car("Test Bus", 200)
    test_bus.drive(30)
    print("fuel =", test_bus.fuel)
    print("odo =", test_bus.odometer)
    test_bus.drive(60)
    print("fuel =", test_bus.fuel)
    print("odo = ", test_bus.odometer)
    print(test_bus)

    # Drive a bus
    print("Enter driving distance:")
    distance = int(input(">> "))
    while distance > 0:
        distance_travelled = test_bus.drive(distance)
        print("{} has travelled {} km.".format(test_bus, distance_travelled))
        print("Enter driving distance (km):")
        distance = int(input(">> "))

    test_taxi = Taxi("Test Taxi", 100)
    print(test_taxi)
    test_taxi.drive(30)
    print(test_taxi, test_taxi.get_fare())
    test_taxi.start_fare()
    test_taxi.drive(60)
    print(test_taxi, test_taxi.get_fare())

    fancy_taxi = Taxi("Test Fancy Taxi", 100, 2)
    print(fancy_taxi)
    fancy_taxi.drive(30)
    print(fancy_taxi, fancy_taxi.get_fare())


if __name__ == '__main__':
    main()