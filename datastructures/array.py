# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None:
        if not isinstance(starting_sequence, (list, np.ndarray)):
            raise ValueError
        for item in starting_sequence:
            if (not isinstance(item, data_type) and (item != data_type)):
                print(item == data_type)
                raise TypeError
        self.__array = np.array(starting_sequence)
        self.__data_type = data_type
        self.__logical_size = self.__array.size
        self.__physical_size = self.__array.size

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if(type(index) != int and type(index) != slice):
            raise TypeError()
        if(type(index) is int and (index >= self.__logical_size or index < 0)):
            raise IndexError()
        if(type(index) is int):
            print(self.__array[index])
            return self.__array[index]
        size = self.__logical_size
        if(type(index) is slice):
            start, stop, step = index.indices(len(self.__array))
            if(start >= size or stop > size or step >= size or start < 0 or  stop < 0 or step < 0):
                raise IndexError()
            myslice = self.__array[start:stop:step] 
            arr = Array(myslice)
            return arr
    
    def __setitem__(self, index: int, item: T) -> None:
        if(not isinstance(item, self.__data_type)):
            raise TypeError
        self.__array[index] = item

    def append(self, data: T) -> None:
        print(self.__logical_size)
        num = self.__physical_size
        if self.__logical_size == num:
            extra__array = np.empty([num*2], None)
            print(extra__array)
            for i in range(num):
                extra__array[i] = self.__array[i]
            extra__array[num] = data
            self.__array = extra__array
            self.__physical_size *= 2
            self.__logical_size += 1
        else:
            self.__array[self.__logical_size] = data
            self.__logical_size += 1
        print(self.__logical_size)

    def append_front(self, data: T) -> None:
        num = self.__physical_size
        if self.__physical_size == self.__logical_size:
            extra__array = np.empty([num*2], None)
            for i in range(num):
                extra__array[i+1] = self.__array[i]
            extra__array[0] = data
            self.__array = extra__array
            self.__physical_size = num*2
            self.__logical_size += 1
        else:
            extra__array2 = np.empty([self.__logical_size+1], None)
            for i in range(self.__logical_size):
                extra__array2[i+1] = self.__array[i]
            extra__array2[0] = data
            self.__array = extra__array2
            self.__logical_size += 1

    def pop(self) -> None:
        self.__array[self.__logical_size-1] = None   
        if self.__logical_size <= (0.25*self.__physical_size):
            extra_array = np.empty[self.__physical_size/2]
            for i in range(self.__logical_size):
                extra_array[i] = self.__array[i]
            self.__array = extra_array
            self.__physical_size /= 2
            self.__logical_size -= 1
        self.__logical_size -= 1
    
    def pop_front(self) -> None:
        self.__array[0] = None
        if self.__logical_size <= (0.25*self.__physical_size):
            extra_array = np.empty([self.__physical_size / 2])
            for i in range(self.__logical_size-1):
                extra_array[i] = self.__array[i+1]
            self.__array = extra_array
            self.__physical_size /= 2
            self.__logical_size -= 1
        else:
            for i in range(self.__logical_size-1):
                self.__array[i] = self.__array[i+1]
            self.__physical_size /= 2
            self.__logical_size -= 1
        self.__logical_size -= 1

    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        if(not isinstance(other, Array)):
            return False
        if(type(other) is None or type(self.__array) is None):
            raise TypeError
        if len(self.__array) != len(other):
            return False
        else:
            for i in range(self.__logical_size):
                if self.__array[i] != other[i]:
                    return False
        print("reached here")
        return True
    
    def __iter__(self) -> Iterator[T]:
        for i in range(len(self.__array)):
            yield self.__array[i]

    def __reversed__(self) -> Iterator[T]:
        for item in reversed(self.__array):
            yield item
            

    def __delitem__(self, index: int) -> None:
        for i in range(index, self.__logical_size - 1):
            self.__array[i] = self.__array[i+1]   
        self.__logical_size -= 1
        if self.__logical_size <= (0.25*self.__physical_size):
            extra_array = np.empty([self.__physical_size])
            for i in range(self.__physical_size/2):
                extra_array[i] = self.__array[i]
            self.__array = extra_array
            self.__physical_size /= 2

    def __contains__(self, item: Any) -> bool:
        for i in range(self.__logical_size):
            if self.__array[i] == item:
                return True
        return False

    def clear(self) -> None:
        list = []
        self.__array = np.array(list)
        self.__physical_size = 0
        self.__logical_size = 0 

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__array)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')