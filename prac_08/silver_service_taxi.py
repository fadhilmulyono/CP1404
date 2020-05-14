"""
CP1404/CP5632 Practical
Silver Service Taxi class, derived from Taxi
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """
    Specialised version of a Taxi that includes fanciness and flagfall fare
    """
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with current fare distance."""
        """
        Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50
        """
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()