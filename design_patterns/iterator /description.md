Building an iterator from scratch is easy in Python. We just have to implement the __iter__() and the __next__()
methods.

The __iter__() method returns the iterator object itself. If required, some initialization can be performed.

The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must
raise StopIteration.