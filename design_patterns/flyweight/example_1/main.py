import random
from enum import Enum

CarType = Enum('CarType', 'subcompact compact suv')


class Car:
    pool = dict()

    def __new__(cls, car_type):
        obj = cls.pool.get(car_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type] = obj
            obj.car_type = car_type
        return obj

    def render(self, color, x, y):
        car_type = self.car_type
        msg = f'render a car of type {car_type} and color {color} at ({x}, {y})'
        print(msg)


def main():
    rnd = random.Random()
    colors = 'white black silver gray red blue brown beige yellow green'.split()
    min_point, max_point = 0, 100
    car_counter = 0

    for _ in range(10):
        c1 = Car(CarType.subcompact)
        c1.render(random.choice(colors),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(3):
        c2 = Car(CarType.compact)
        c2.render(random.choice(colors),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(5):
        c3 = Car(CarType.suv)
        c3.render(random.choice(colors),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    print(f'cars rendered: {car_counter}')
    print(f'cars actually created: {len(Car.pool)}')

    c4 = Car(CarType.subcompact)
    c5 = Car(CarType.subcompact)
    c6 = Car(CarType.suv)
    print(f'{id(c4)} == {id(c5)}? {id(c4) == id(c5)}')
    print(f'{id(c5)} == {id(c6)}? {id(c5) == id(c6)}')


if __name__ == '__main__':
    """
    The main() function shows how we can use the flyweight pattern. The color of a car is a
    random value from a predefined list of colors. The coordinates use random values between
    1 and 100. Although 18 cars are rendered, memory is allocated only for three. The last line
    of the output proves that when using flyweight, we cannot rely on object identity. The id()
    function returns the memory address of an object. This is not the default behavior in Python
    because by default, id() returns a unique ID (actually the memory address of an object as
    an integer) for each object. In our case, even if two objects appear to be different, they
    actually have the same identity if they belong to the same flyweight family (in this case,
    the family is defined by car_type). Of course, different identity comparisons can still be
    used for objects of different families, but that is possible only if the client knows the
    implementation details.
    """
    main()
