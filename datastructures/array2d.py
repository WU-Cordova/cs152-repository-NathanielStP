from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.__rowNum = row_index
            self.__rowLength = num_columns
            self.__array = array
            self.__convert = self.__rowLength*self.__rowNum
            

        def __getitem__(self, column_index: int) -> T:
            return self.__array[self.__convert + column_index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            self.__array[self.__convert + column_index] = value
        
        def __iter__(self) -> Iterator[T]:
            for i in range(self.__convert, self.__rowLength+self.__convert):
                yield self.__array[i]
        
        def __reversed__(self) -> Iterator[T]:
            myrow = self.__array[self.__convert:self.__convert+self.__rowLength]
            for item in reversed(myrow):
                yield item

        def __len__(self) -> int:
            return self.__rowLength
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.__rowLength)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.__rowNum}: [{", ".join([str(self[column_index]) for column_index in range(self.__rowLength - 1)])}, {str(self[self.__rowLength - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if(starting_sequence not isinstance(Sequence)):
            raise ValueError
        for i in range(1, len(starting_sequence)):
            if type(starting_sequence[i]) != type(starting_sequence[i-1]):
                raise ValueError
        firstdimension = [item for row in starting_sequence for item in row]
        print(firstdimension)
        self.__array = Array(firstdimension, data_type)
        self.__data_type = data_type
        self.__num_rows = len(starting_sequence)
        self.__num_cols = len(starting_sequence[0])

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        for i in range(rows):
            for x in range(cols):
                myarr = Array2D[i][x] = data_type
        return myarr


    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return self.__array[row_index]
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for i in range(self.__num_rows):
            for x in range(self.__num_cols):
                yield self.__array[i][x]
    
    def __reversed__(self):
        for i in range(self.__num_rows):
            for x in range(self.__num_cols):
                yield self.__array[self.__num_rows - 1 - i][self.__num_cols - 1 - x]
    
    def __len__(self): 
        return self.__num_rows
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_cols} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')