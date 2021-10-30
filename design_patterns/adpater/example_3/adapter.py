from pegs import SquarePeg, RoundPeg


class SquareAdapter(RoundPeg):
    """SquareAdapter class lets you fit square pegs into round holes.
    It extends the RoundPeg class to let the adapter objects act as round pegs.

    This adapter makes RoundPeg behave like SquarePeg.
    """

    def __init__(self, peg: SquarePeg):
        self.peg = peg
        super().__init__(radius=self.peg.get_width() / (2 ** 0.5))
