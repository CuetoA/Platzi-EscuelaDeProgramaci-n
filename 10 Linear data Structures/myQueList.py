class MyQue:
    def __init__(self) -> None:
        self.items = []
        self.size = len(self.items)
        pass

    def enqueue(self, data):
        self.items.append(data)
        
    def dequeue(self):
        self.items.pop(0)

    def transverse():
        
