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
        if starting_sequence is not Sequence:
            raise ValueError()
        if data_type is not object:
            raise ValueError()
        self.__array = np.array[starting_sequence]
        self.__data_type = data_type
        self.__logical_size = self.__array.size
        self.__physical_size = self.__array.size

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if index is int:
            return self.__array[index]
         
        if index is slice:
            return self.__array[slice]
    
    def __setitem__(self, index: int, item: T) -> None:
        self.__array[index] = item

    def append(self, data: T) -> None:
        num = self.__physical_size
        if self.__logical_size == self.__physical_size:
            extra__array = np.array[data*num*2]
            for i in range(num*2):
                if(i >= num):
                    extra__array[i] = None
                else:
                    extra__array[i] = self.__array[i]
            extra__array[num] = data
            self.__array = extra__array
            self.__physical_size = num*2
            self.__logical_size = self.__logical_size + 1
        else:
            self.__array[self.__logical_size] = data
            self.__logical_size = self.__logical_size + 1

    def append_front(self, data: T) -> None:
        num = self.__physical_size
        if self.__physical_size == self.__logical_size:
            extra__array = np.array[data*num*2]
            for i in range(num):
                extra__array[i+1] = self.__array[i]
            extra__array[0] = data
            self.__array = extra__array
            self.__physical_size = num*2
            self.__logical_size = self.__logical_size + 1
        else:
            extra__array2 = np.array
            for i in range(num):
                extra__array2[i+1] = self.__array[i]
            extra__array2[0] = data
            self.__array = extra__array2
            self.__logical_size = self.__logical_size + 1

    def pop(self) -> None:
        self.__array[self.__logical_size-1] = None   
        if self.__logical_size < (0.25*self.__physical_size):
            extra_array = np.array[0]
            for i in range(self.__physical_size/2):
                extra_array.append(self.__array[i])
            self.__array = extra_array
            self.__physical_size = self.__physical_size / 2
            self.__logical_size = self.__logical_size - 1
        self.__logical_size = self.__logical_size - 1
    
    def pop_front(self) -> None:
        self.__array[0] = None
        if self.__logical_size < (0.25*self.__physical_size):
            extra_array = np.array[0]
            for i in range(self.__physical_size/2):
                extra_array.append(self.__array[i])
            self.__array = extra_array
            self.__physical_size = self.__physical_size / 2
            self.__logical_size = self.__logical_size - 1
        self.__logical_size = self.__logical_size - 1

    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        if self.__len__ != other.__len__:
            return False
        else:
            for i in range(self.__len__):
                if self.__array[i] != other[i]:
                    return False
        return True
    
    def __iter__(self) -> Iterator[T]:
        return self.__array[T]

    def __reversed__(self) -> Iterator[T]:
        extra_array = self.__array
        for i in range(self.__logical_size):
            extra_array[self.__logical_size-1-i] = self.__array[i]
        self.__array = extra_array
            

    def __delitem__(self, index: int) -> None:
        self.__array[index] = None
        i = index
        for i in range(self.__logical_size):
            self.__array[i] = self.__array[i+1]   
        if self.__logical_size < (0.25*self.__physical_size):
            extra_array = np.array[0]
            for i in range(self.__physical_size/2):
                extra_array.append(self.__array[i])
            self.__array = extra_array
        self.__logical_size = self.__logical_size - 1

    def __contains__(self, item: Any) -> bool:
        for i in range(self.__logical_size):
            if self.__array[i] == item:
                return True
        return False

    def clear(self) -> None:
        self.__array = np.array[]

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')