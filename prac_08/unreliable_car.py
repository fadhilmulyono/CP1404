"""
CP1404/CP5632 Practical
Unreliable Car class, derived from Car
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """
    UnreliableCar has an additional attribute:
    reliability: a float between 0 and 100, that represents the percentage chance that the drive method will actually work
    """
    def __init__(self, name, fuel, reliability):
        """call the Car's version of __init__, and then set the reliability to the value passed in"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """generate a random number between 0 and 100"""
        random_number = randint(0, 100)
        # only drive the car if that number is less than the car's reliability
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
