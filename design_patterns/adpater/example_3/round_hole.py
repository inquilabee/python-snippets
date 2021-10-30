from pegs import RoundPeg


class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg: RoundPeg):
        """Returns if the said (round) peg fit into the current round hole."""
        # Note that the method is expecting an object which implements get_radius method.
        return self.get_radius() >= peg.get_radius()
