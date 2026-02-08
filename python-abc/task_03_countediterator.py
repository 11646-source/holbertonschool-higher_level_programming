
"""
CountedIterator class that wraps an iterable and
tracks how many items have been iterated.
"""


class CountedIterator:
    """Iterator that counts the number of items fetched."""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)  # May raise StopIteration
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self._count


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    counted_iter = CountedIterator(numbers)

    for num in counted_iter:
        print("Got:", num)

    print("Total items fetched:", counted_iter.get_count())
