"""
Reference: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
"""


class SingletonObject:
    instance = None

    class __SingletonObject:
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, key, val):
        return setattr(self.instance, key, val)


if __name__ == '__main__':
    x = SingletonObject()
    y = SingletonObject()
    z = SingletonObject()

    x.val = 'sausage'
    y.val = 'eggs'
    z.val = 'spam'

    print(x)
    print(y)
    print(z)
