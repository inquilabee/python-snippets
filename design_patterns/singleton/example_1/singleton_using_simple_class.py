class SingletonStudent(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not SingletonStudent._instance:
            SingletonStudent._instance = object.__new__(cls)
        return SingletonStudent._instance

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


if __name__ == '__main__':
    s1 = SingletonStudent("Yang", "Zhou")
    s2 = SingletonStudent("Elon", "Musk")

    print(s1)
    print(s2)
    print(s1 == s2, s1 is s2)
    print(s1.first_name, s1.last_name)
    print(s2.first_name, s2.last_name)
