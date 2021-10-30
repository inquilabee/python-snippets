"""
Adapted from: https://github.com/faif/python-patterns/blob/master/patterns/creational/builder.py
"""
from houses import House, Flat, Room, ComplexHouse
from director import BuildingDirector


def main():
    # Building ourselves, complex and difficult to remember the steps
    room = Room()
    room.build_floor()
    room.build_size()

    # Constructor building the objects using Builder class
    house = House()
    flat = Flat()

    # Using a director class to handle building
    director = BuildingDirector(ComplexHouse)
    complex_house = director.construct_building()  # Using an external constructor function:

    print(house)
    print(flat)
    print(room)
    print(complex_house)


if __name__ == "__main__":
    main()
