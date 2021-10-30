"""
Strategy Pattern:

Most problems can be solved in more than one way. Take, for example, the sorting
problem, which is related to putting the elements of a list in a specific order.
There are many sorting algorithms, and, in general, none of them is considered
the best for all cases.

One can chose a strategy to sort some items based on some criteria. Strategy Pattern
lets us do just that.

In the example, we try to find if a word has repeating characters using different
strategy.

Adapted from: Mastering Python Design Patterns, Second Edition, Packt Publication
"""

import time

SLOW = 3  # in seconds
LIMIT = 5  # in characters
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def all_unique_sort(s) -> bool:
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    sorted_str = sorted(s)

    for c1, c2 in pairs(sorted_str):
        if c1 == c2:
            return False
    return True


def all_unique_set(s) -> bool:
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def all_unique(word, strategy):
    return strategy(word)


if __name__ == '__main__':
    all_strategies = {
        "1": all_unique_set,
        "2": all_unique_sort,
    }

    word = "something"

    for strategy_number in ["1", "2"]:
        strategy = all_strategies[strategy_number]

        print(all_unique(word=word, strategy=strategy))
