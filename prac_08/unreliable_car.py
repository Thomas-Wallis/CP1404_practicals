"""
Car class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        Car will only work sometimes based on reliability.
        """
        if random.randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            pass
        return distance
