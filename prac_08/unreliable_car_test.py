"""
CP1404/CP5632 Practical
Test Unreliable Car
"""
from prac_08.unreliable_car import UnreliableCar


def main():
    # Create several cars
    car_1 = UnreliableCar("Fast Racer", 100, 88)
    car_2 = UnreliableCar("Azure Racer", 100, 66)
    car_3 = UnreliableCar("Red Danger", 100, 44)
    car_4 = UnreliableCar("Good Oldie", 100, 22)

    # Attempt to drive the cars
    for i in range(1, 13):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(car_1.name, car_1.drive(i)))
        print("{:12} drove {:2}km".format(car_2.name, car_2.drive(i)))
        print("{:12} drove {:2}km".format(car_3.name, car_3.drive(i)))
        print("{:12} drove {:2}km".format(car_4.name, car_4.drive(i)))
        print("\n")

    # Print details of all cars
    print("Car details")
    print(car_1)
    print(car_2)
    print(car_3)
    print(car_4)


if __name__ == '__main__':
    main()