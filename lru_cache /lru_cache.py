"""
Usually, you will use lru_cache from functools module.
   from functools import lru_cache

Below is an attempt to implement the same using dictionary for educational purposes.
"""


class LRUCache:
    """LRU Cache using dictionary (works in Python 3.7+)"""

    def __init__(self, maxsize: int = 128):
        if maxsize < 1:
            raise Exception("Size of cache can not be less than 1")

        self.maxsize = maxsize
        self.cache = {}

    def __len__(self):
        return len(self.cache)

    def __str__(self):
        return str(tuple(self.cache.items()))

    @property
    def size(self) -> int:
        """returns the size of the cache"""
        return len(self)

    def put(self, key, val):
        if self.size == self.maxsize:
            self._remove_least_recently_used_key()

        # TODO: What to do if key already exist in the cache? Override?
        self.cache[key] = val

    def get(self, key):
        if key in self.cache:
            self._move_key_to_end(key)
            return self.cache[key]
        return None

    def _remove_least_recently_used_key(self):
        """Evicts the least recently used item from the cache"""
        self._remove_first_key()

    def _remove_first_key(self):
        first_item = list(self.cache.keys())[0]
        self.cache.pop(first_item)

    def _move_key_to_end(self, key):
        self.cache[key] = self.cache.pop(key)


if __name__ == '__main__':
    cache = LRUCache(maxsize=2)
    cache.put(1, 1)
    print(cache)

    cache.put(2, 2)
    print(cache)

    cache.get(1)
    print(cache)

    cache.put(3, 3)
    print(cache)

    cache.get(2)
    print(cache)

    cache.put(4, 4)
    print(cache)

    cache.get(1)
    print(cache)

    cache.get(3)
    print(cache)

    cache.get(4)
    print(cache)

    print(len(cache))
    print(cache.size)
