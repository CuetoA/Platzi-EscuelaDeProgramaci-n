from hashlib import new
from myarray import MyArray

class StackArr(MyArray):

    def __init__(self, capacity, fill_value=None):
        super().__init__(capacity, fill_value)

    def push(self, data):
        index = self.getSize()
        self.__setitem__(index, data)     

    def pop(self):
        index = self.getSize() -1
        self.__setitem__(index, None)

    def peek(self):
        index = self.getSize() -1
        return self.items[index]

    def clearStack(self):
        for index in range( self.getSize() ):
            self.items[index] = None
        
    def isElement(self, data):
        for index in range( self.getSize() ):
            if self.items[index] == data:
                return True
        return False


if __name__ == "__main__":
    my_stack = StackArr(10)

    for i in range(5):
        my_stack.__setitem__(i, f"{i}")
    
    my_stack.printArr()
    my_stack.push("a")
    my_stack.push("b")
    my_stack.push("c")
    my_stack.push("d")
    my_stack.printArr()
    print( f"In the peak is: {my_stack.peek()}")
    element = "c"
    print( f"Is the element {element} in the Stack? {my_stack.isElement(element)}\n")


    my_stack.pop()
    my_stack.pop()
    my_stack.printArr()
    print( f"In the peak is: {my_stack.peek()}")
    print( f"Is the element {element} in the Stack? {my_stack.isElement(element)}\n")

    my_stack.clearStack()
    my_stack.printArr()
