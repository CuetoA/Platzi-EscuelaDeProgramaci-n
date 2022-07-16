from mylinkedlist import LinkedList
from mynode import Node

class CircularLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def append(self, data):
        super().append(data, self.head)
        


if __name__ == "__main__":
    print('Managing my own Linked List'.center(100, '-'))

    words = CircularLinkedList()
    words.append("Eggs")
    words.append("Meat")
    words.append("Pinaple")
    words.append("Watermelon")

    print("\nAfter append:")
    words.myPrint()

    print(f"\nSize: {words.size}")

    print("\nDeleting:")
    words.delete("Meat")
    words.myPrint()

    print("\nClrear:")
    words.clear()
    words.myPrint()