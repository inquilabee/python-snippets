class ListIterator:
    def __init__(self, list_object: list):
        self.list_object = list_object
        self.index = -1

    def __next__(self):
        self.index = self.index + 1
        if self.index < len(self.list_object):
            return self.list_object[self.index]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class InfiniteOddIterator:
    """Infinite iterator to return all
        odd numbers"""

    def __init__(self):
        self.num = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        return self.num


if __name__ == '__main__':
    x = list(range(10))

    list_iterator = ListIterator(x)

    for item in list_iterator:
        print(item)

    y = list(range(10))

    list_iterator = ListIterator(y)

    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))

    odd_iter = InfiniteOddIterator()

    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
    print(next(odd_iter))
