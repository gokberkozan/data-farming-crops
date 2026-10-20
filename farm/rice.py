"""Rice crop."""
from farm.crop import Crop


class Rice(Crop):
    """Rice: each watering adds 5 grains, transplanting adds 10."""

    def water(self):
        """Water the rice, adding 5 grains."""
        self.grains += 5

    def transplant(self):
        """Transplant the rice, adding 10 grains."""
        self.grains += 10
