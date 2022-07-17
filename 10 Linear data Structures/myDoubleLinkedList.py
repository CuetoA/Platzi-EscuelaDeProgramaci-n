import ctypes
from mynode import Node

class doubleNode(Node):
    def __init__(self, data, next = None, prevous = None):
        super().__init__(data, next)
        self.previous = None



class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0


    def append(self, data):
        node = doubleNode(data)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            last = self.tail
            node.previous = last
            last.next = node
            self.tail = node
        self.size += 1
    

    def delete(self, data):
        current = self.head
        previous = self.head
        i = self.size

        while current and i>=0:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    print(f"deleted: {current.data}")

            i -= 1
            previous = current
            current = current.next


    def iter(self):
        current = self.head
        i = self.size

        while current and i>=0:
            node = current
            current = current.next
            i -= 1
            yield node


    def searchForward(self, data):
        current = self.head

        while current:
            if current.data == data:
                print(f"data \"{data}\" found in element {id(current)}")
                return 1
            current = current.next
        print(f"data \"{data}\" not found")
        return 0

    
    def searchBackward(self, data):
        current = self.tail

        while current:
            if current.data == data:
                print(f"data \"{data}\" found in element {id(current)}")
                return 1
            current = current.previous
        print(f"data \"{data}\" not found")
        return 0


    def myPrint(self):
        myStr = ""
        for element in self.iter():
            myStr += f"[{id(element.previous)} ,{element.data}, {id(element.next)}] -> \n"

        print(myStr)
        print()
    

    def printMemory(self):
        print("Data \t\t\t Memory address  \t\t Previous Mem. A \t\t Next Mem. A")

        for element in self.iter():
            data = element.data
            memoryAdress = id(element)
            previousNode = id(element.previous) if element.previous else "None \t\t"
            nextNode = id(element.next) if element.next else "None \t"

            print(f"{data} \t\t {memoryAdress} \t\t {previousNode} \t\t {nextNode}")
        print()






if __name__ == "__main__":
    myLinked = DoubleLinkedList()

    myLinked.append("hello  ")
    myLinked.append("there  ")
    myLinked.append("how are")
    myLinked.append("you my ")
    myLinked.append("fiend? ")
    
    myLinked.printMemory()
    
    myLinked.myPrint()

    myLinked.searchForward("there  ")
    myLinked.searchForward("nonestop")

    myLinked.searchForward("you my ")
    myLinked.searchForward("nonestop")

    myLinked.delete("you my ")
    myLinked.myPrint()