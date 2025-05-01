import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self.data_type = data_type
        mylist = [data_type]*max_size
        self.__size = max_size
        self.__stack = Array[data_type](mylist, data_type)
        self.__top = -1 

    def push(self, item: T) -> None:
        self.__top += 1
        self.__stack[self.__top] = item

    def pop(self) -> T:
        item = self.__stack[self.__top]
        self.__stack.pop()
        self.__top -= 1
        return item

    def clear(self) -> None:
       self.__top = -1
       self.__stack.clear()
       print(self.__stack)

    @property
    def peek(self) -> T:
       return self.__stack[self.__top]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.__size   
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self.__top == self.__size - 1
        

    @property
    def empty(self) -> bool:
        return self.__top == -1
    
    def __eq__(self, other: object) -> bool:
        for i in range(len(other)):
            if other.pop() != self.pop(): 
                return False
        return True

    def __len__(self) -> int:
       return self.__top + 1
    
    def __contains__(self, item: T) -> bool:
        for thing in self.__stack:
           if thing == item:
               return True
        return False
           

    def __str__(self) -> str:
        return str([self.__stack[i] for i in range(self.__top + 1)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.__size}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

