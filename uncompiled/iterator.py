from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalIterator(Iterator):
    """
    Class that realize iterator in alphabetical order for any iterable collection

    """

    def __init__(self, iterable_object: object, reverse: bool = False) -> None:
        """
        Initialize iterator for iterable collection

        :param iterable_object: object to iterate
        :param reverse: reverse or not iteration order
        """
        self._current_index = -1 if reverse else 0
        self._collection = iterable_object
        self._reverse = reverse

    def __next__(self) -> object:
        """
        Returns next object in alphabetical order

        :return: next object of collection
        """
        try:
            value = self._collection[self._current_index]
            self._current_index += -1 if self._reverse else 1

        except IndexError:
            raise StopIteration()

        return value


class IterableCollection(Iterable):
    """
    Iterable collection with list type to implement Iterator pattern

    """

    def __init__(self, collection: List[Any] = None) -> None:
        self._collection = [] if collection is None else collection

    def __iter__(self) -> AlphabeticalIterator:
        """
        Returns iterator object

        :return: iterator
        """
        return AlphabeticalIterator(self._collection)

    def __reversed__(self) -> AlphabeticalIterator:
        """
        Returns reversed iterator object

        :return: reversed iterator
        """
        return AlphabeticalIterator(self._collection, True)

    def push(self, item: Any):
        self._collection.append(item)


def main():
    collection = IterableCollection()
    collection.push("Red")
    collection.push("Orange")
    collection.push("Green")

    print("\nDefault order: {")
    print("\n".join(collection), end="\n}\n")

    reversed_collection = reversed(collection)
    print("Reversed order: {")
    print("\n".join(reversed_collection), end="\n}\n")


if __name__ == "__main__":
    main()
