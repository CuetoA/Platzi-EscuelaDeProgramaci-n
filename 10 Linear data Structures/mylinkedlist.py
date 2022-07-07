from mynode import Node


class LinkedList:
    def __init__(self) -> None:
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next
            current.next = node

        self.size += 1

    def size(self):
        return str(self.size)

    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

