class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state=None):
        super().__init__()

        if not hasattr(self, "state"):
            self.state = "Init"

        if state:
            self.state = state

    def __str__(self):
        return f"State: {self.state}"


class NeighboursBorg(Borg):
    def __init__(self, neighbourhood=None):
        super().__init__()

        if not hasattr(self, "neighbourhood"):
            self.neighbourhood = "NY"

        if neighbourhood:
            self.neighbourhood = neighbourhood

    def __str__(self):
        return f"Neighbourhood: {self.neighbourhood}"


if __name__ == '__main__':
    x = Borg()
    y = Borg()

    x.state = 'Idle'
    y.state = 'Running'

    print(f"x : {x}")
    print(f"y : {y}")

    y.state = 'Zombie'

    print(f"x : {x}, id : {id(x)}")
    print(f"y : {y}, id : {id(y)}")

    z = YourBorg()

    print(f"x : {x}, id : {id(x)}")
    print(f"y : {y}, id : {id(y)}")
    print(f"z : {z}, id : {id(z)}")

    w = YourBorg(state="Havoc")

    print(f"x : {x}, id : {id(x)}")
    print(f"y : {y}, id : {id(y)}")
    print(f"z : {z}, id : {id(z)}")
    print(f"z : {w}, id : {id(w)}")

    k = NeighboursBorg()

    print(f"k : {k}, id : {id(k)}")

    m = NeighboursBorg("LA")

    print(f"m : {m}, id : {id(m)}")
