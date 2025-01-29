from typing import Iterable, Optional
from ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bag: dict[T, int] = {}

        if items != None:
            for item in items:
                self.add(item)

    def add(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1

    def remove(self, item: T) -> None:
        self.__bag[item] -= 1

    def count(self, item: T) -> int:
        return self.__bag.get(item)

    def __len__(self) -> int:
        return len(self.__bag)

    def distinct_items(self) -> Iterable[T]:
        return self.__bag.keys()

    def __contains__(self, item) -> bool:
        if item in self.__bag:
            return True
        else: return False

    def clear(self) -> None:
        self.__bag.clear()