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
        new_tail = self.tail.previous
        self.delete(data)
        self.tail = new_tail


    def peek(self):
        if self.tail:
            data = self.tail.data
            print(f"Top data is {data}")
        else:
            print("The stack is empty")


    def clearStack(self):
        while self.tail:
            self.pop()
        



if __name__ == "__main__":
    newStack = Stack()

    newStack.append("hey")
    newStack.append("kid")
    newStack.append("do ")
    newStack.append("I  ")
    newStack.append("have")
    newStack.append("your")
    newStack.append("attention")

    newStack.myPrint()

    newStack.pop()
    newStack.myPrint()
    newStack.peek()

    newStack.pop()
    newStack.myPrint()
    newStack.peek()

    newStack.clearStack()
    newStack.myPrint()