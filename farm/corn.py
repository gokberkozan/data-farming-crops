"""Corn crop."""
from farm.crop import Crop


class Corn(Crop):
    """Corn: each watering adds 10 grains."""

    def water(self):
        """Water the corn, adding 10 grains."""
        self.grains += 10
