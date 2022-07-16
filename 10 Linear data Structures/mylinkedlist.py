from calendar import day_abbr
from mynode import Node


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0


    def append(self, data):
        node = Node(data)

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


    def size(self):
        return str(self.size)


    def iter(self):
        current = self.head
        i = self.size

        while current and i>=0:
            val = current.data
            
            try:
                next_node = current.next
            except:
                next_node = None

            current = current.next
            i -= 1
            yield val, next_node


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


    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(f"data {data} found in node {current}")
                # return current
            current = current.next


    def clear(self):
        self.head = None
        self.size = 0


    def myPrint(self):
        myStr = ""
        for element in self.iter():
            myStr += f"[{element[0]}, {element[1]}] -> "

        print(myStr)


if __name__ == "__main__":
    print('Managing my own Linked List'.center(100, '-'))

    words = LinkedList()
    words.append("Eggs")
    words.append("Meat")
    words.append("Pinaple")
    words.append("Grapes")
    words.append("Apple")
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