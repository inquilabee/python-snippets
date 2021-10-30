class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(*args, **kwargs)
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    x = SingletonClass()
    y = SingletonClass()

    print(x == y, x is y)
