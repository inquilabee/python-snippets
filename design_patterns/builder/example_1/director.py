class BuildingDirector:
    def __init__(self, builder):
        self.__builder = builder

    def construct_building(self):
        building = self.__builder()
        building.build_floor()
        building.build_size()
        return building
