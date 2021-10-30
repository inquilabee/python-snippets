import config
from util_one import make_twice
from util_two import make_thrice

if __name__ == '__main__':
    print(config.x)
    config.x = 2
    print(config.x)
    make_twice()
    make_thrice()
    print(config.x)
