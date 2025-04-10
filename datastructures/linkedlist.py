from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterator, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        if not all(isinstance(item, data_type) for item in sequence):
            raise TypeError
        mylist = LinkedList(data_type=data_type)
        for item in sequence:
            mylist.append(item)
        return mylist

    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        node = LinkedList.Node(data=item)
        if self.empty:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            if self.tail:
                self.tail.next = node
            self.tail = node
        self.count += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        node = LinkedList.Node(data=item)
        if self.empty:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            if self.head:
                self.head.previous = node
            self.head = node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type) or not isinstance(item, self.data_type):
            raise TypeError
        if target not in self:
            raise ValueError
        travel = self.head
        while travel:
            if travel.data == target:
                node = LinkedList.Node(data=item)
                node.next = travel
                node.previous = travel.previous
                node.previous.next = node
                travel.previous = node
                self.count += 1
            travel = travel.next
            

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type) or not isinstance(item, self.data_type):
            raise TypeError
        if target not in self:
           raise ValueError
        travel = self.tail
        while travel:
            if travel.data == target:
                node = LinkedList.Node(data=item)
                node.previous = travel
                node.next = travel.next
                node.next.previous = node
                travel.next = node
                self.count += 1
            travel = travel.previous

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        if item not in self:
            raise ValueError
        travel = self.tail
        while travel:
            if len(self) == 1 and self.head.data == item:
                self.pop()
            elif item == self.tail.data:
                print(str(self.count) + " count")
                self.tail.previous.next = None
                self.tail = self.tail.previous
                self.count -= 1
            elif travel.data == item:
                travel.previous.next = travel.next
                travel.next.previous = travel.previous
                self.count -= 1
            travel = travel.previous

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        while item in self:
            print(self.tail.data)
            self.remove(item)

    def pop(self) -> T:
        if self.empty:
            raise IndexError
        if len(self) == 1:
            self.count = 0
            data = self.tail.data
            self.head = None
            self.tail = None
            return data
        data = self.tail.data
        self.tail.previous.next = None
        self.tail = self.tail.previous
        self.count -= 1
        return data

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError
        data = self.head.data
        self.head.next.previous = None
        self.head = self.head.next
        self.count -= 1
        return data

    @property
    def front(self) -> T:
        if self.head:
            return self.head.data
        raise IndexError

    @property
    def back(self) -> T:
        if self.tail:
            return self.tail.data
        raise IndexError

    @property
    def empty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        return self.count 
    
    def clear(self) -> None:
        self.count = 0
        self = None        

    def __contains__(self, item: T) -> bool:
        current = self.tail
        while current:
            if current.data == item:
                return True
            current = current.previous
        return False

    def __iter__(self) -> Iterator[T]:
        self.travel_node = self.head
        return self 
    
    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        self.travel_node = self.tail
        helper = []
        if self.travel_node is None:
            raise StopIteration
        while self.travel_node:
            data = self.travel_node.data
            self.travel_node = self.travel_node.previous
            helper.append(data)
        return helper
    
    def __eq__(self, other: object) -> bool:
        list1 = list(reversed(self))
        list2 = list(reversed(other))
        return list1 == list2

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
