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
            self.__convert = self.__rowLength*self.__rowNum
            self.__array = array
            self.__row = array[self.__rowNum * self.__rowLength: 
                               (self.__rowNum + 1) * self.__rowLength]

        def __getitem__(self, column_index: int) -> T:
            return self.__row[column_index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            self.__row[column_index] = value
            self.__array[self.__convert + column_index] = value
        
        def __iter__(self) -> Iterator[T]:
            print("here")
            for item in self.__row:
                yield item
        
        def __reversed__(self) -> Iterator[T]:
            myrow = self.__row[self.__convert:self.__convert+self.__rowLength]
            for item in reversed(myrow):
                yield item

        def __len__(self) -> int:
            return self.__rowLength
        
        def __str__(self) -> str:
            return f"[{', '.join(map(str, self.__row))}]"
        
        def __repr__(self) -> str:
            return f'Row {self.__rowNum}: [{", ".join([str(self[column_index]) for column_index in range(self.__rowLength - 1)])}, {str(self[self.__rowLength - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, list) or not all(isinstance(item, list) for item in starting_sequence):
            raise ValueError
        if not all(isinstance(row, list) for row in starting_sequence):
            raise ValueError
        row_length = {len(row) for row in starting_sequence}
        if(len(row_length) > 1):
            raise ValueError
        element_type = (type(starting_sequence[0][0]))
        for row in starting_sequence:
            for item in row:
                if not isinstance(item, element_type):
                    raise ValueError 
        firstdimension = [item for row in starting_sequence for item in row]
        self.__array = Array(firstdimension, data_type)
        self.__num_rows = len(starting_sequence)
        self.__num_cols = len(starting_sequence[0])

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        return Array2D([[0]*cols for _ in range(rows)], data_type)


    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        row = self.Row(row_index, self.__array, self.__num_cols)
        return row
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        print("inside iter")
        for i in range(self.__num_rows):
            yield self.Row(i, self.__array, self.__num_cols)
    
    def __reversed__(self):
        for i in range(self.__num_rows - 1, -1, -1):
            yield self.Row(i, self.__array, self.__num_cols)
    
    def __len__(self): 
        return self.__num_rows
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(str(self.Row(i, self.__array, self.__num_cols)) for i in range(self.__num_rows))}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_cols} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')