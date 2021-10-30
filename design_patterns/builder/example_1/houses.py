from core import BaseBuilding, BasicBuilding


class Room(BasicBuilding):
    floor = -1
    size = -1

    def build_floor(self):
        self.floor = "A section of the floor"

    def build_size(self):
        self.size = "Half of usual room flat size"


class House(BaseBuilding):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big"


class Flat(BaseBuilding):
    def build_floor(self):
        self.floor = "More than One"

    def build_size(self):
        self.size = "Small"


class ComplexHouse(BaseBuilding):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big and fancy"
