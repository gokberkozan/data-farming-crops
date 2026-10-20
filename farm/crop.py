# pylint: disable=too-few-public-methods
"""Parent class shared by all crops on the farm."""


class Crop:
    """A generic crop that grows grains."""

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True if the crop has at least 15 grains."""
        return self.grains >= 15
