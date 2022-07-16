from mylinkedlist import LinkedList
from mynode import Node

class CircularLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def append(self, data):
        node = Node(data, self.head)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            i = self.size

            while current.next and i>=0:
                current = current.next
                i -= 1
            current.next = node

        self.size += 1


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