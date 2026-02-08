#!/usr/bin/python3
"""
VerboseList class that extends list and prints notifications
for append, extend, remove, and pop operations.
"""


class VerboseList(list):
    """A list subclass that prints messages on modifications."""

    def append(self, item):
        """Append item and print a notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend list and print how many items were added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """Print a notification before removing an item."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification before popping an item."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


if __name__ == "__main__":
    vlist = VerboseList([1, 2, 3])
    vlist.append(4)
    vlist.extend([5, 6])
    vlist.remove(2)
    vlist.pop()
    vlist.pop(0)
