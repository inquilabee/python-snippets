from round_hole import RoundHole
from pegs import RoundPeg, SquarePeg
from adapter import SquareAdapter

if __name__ == '__main__':
    hole = RoundHole(radius=5)

    round_peg = RoundPeg(radius=4)
    square_peg = SquarePeg(width=5)

    print(hole.fits(round_peg))
    # print(hole.fits(square_peg)) # AttributeError: 'SquarePeg' object has no attribute 'get_radius'

    square_peg_adapter = SquareAdapter(square_peg)

    print(hole.get_radius(), square_peg_adapter.get_radius())

    print(hole.fits(square_peg_adapter))
