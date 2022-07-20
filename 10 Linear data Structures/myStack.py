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
        
    
    def isElement(self, data):
        for element in self.iter():
            if element.data == data:
                return True
        return False
        



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

    element1 = "hey"
    print(f'\nChecking if element \"{element1}\" is in stack: {newStack.isElement(element1)}')

    element2 = "attention"
    print(f'\nChecking if element \"{element2}\" is in stack: {newStack.isElement(element2)}')

    newStack.clearStack()
    newStack.myPrint()