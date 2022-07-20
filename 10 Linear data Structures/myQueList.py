class MyQue:
    def __init__(self) -> None:
        self.items = []
        self.size  = len(self.items)
        pass

    def enqueue(self, data):
        self.items.append(data)
        self.size += 1
        
    def dequeue(self):
        poped = self.items.pop(0)
        self.size -= 1
        return poped

    def transverse(self):
        total_items = self.size
        message = ""

        for item in range(total_items):
            # print(f"item is {item}")
            message += str(self.items[item]) + ", "
        print(message)


if __name__ == "__main__":
    food = MyQue()
    food.enqueue("eggs")
    food.enqueue("hotdog")
    food.enqueue("tamarindo")
    food.enqueue("wings")
    food.enqueue("milk")
    food.enqueue("jam")
    food.transverse()

    print(food.dequeue())
    print(food.dequeue())
    food.transverse()
