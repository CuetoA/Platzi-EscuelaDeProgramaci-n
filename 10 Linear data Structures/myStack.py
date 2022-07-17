import ctypes
from mynode import Node
from myDoubleLinkedList import DoubleLinkedList

class Stack(DoubleLinkedList):
    def __init__(self) -> None:
        super().__init__()
        
    def push(self, data):
        self.append(data)

    def pop(self):
        data = self.tail.data
        print(f"THis is the data at the final: {data}")



if __name__ == "__main__":
    newStack = Stack()

    newStack.append("hey")
    newStack.append("kid")
    newStack.append("do ")
    newStack.append("you")

    newStack.myPrint()

    newStack.pop()