import random
import bisect

if __name__ == '__main__':

    a = sorted(random.sample(range(10, 100), 20))
    positions = random.sample(range(10, 90), 10)

    print(a)
    print(positions)

    for pos in positions:
        print(pos, bisect.bisect_left(a, pos), bisect.bisect_right(a, pos), bisect.bisect(a, pos))

    for pos in positions:
        bisect.insort_left(a, pos)
        print(pos, a)
