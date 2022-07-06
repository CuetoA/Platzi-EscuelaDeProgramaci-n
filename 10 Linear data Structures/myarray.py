"""Created our own array class
"""

class MyArray():
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
        
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)
    
    def __getIntem__(self, index):
        return self.items[index]

    def __setIntem__(self, index, newIntem):
        self.items[index] = newIntem

    def __sum__(self):
        for i in range(self.__len__()):
            if i == 0:  sum  = self.items[i]
            else:       sum += self.items[i]
        return sum
        

if __name__ == "__main__":
    menu = MyArray(5)
    print(menu.__len__())
    print(menu.__str__())
    print(menu.__iter__())
    menu.__setIntem__(0, 0)
    menu.__setIntem__(1, 2)
    menu.__setIntem__(2, 4)
    menu.__setIntem__(3, 8)
    menu.__setIntem__(4, 16)
    print(menu.__getIntem__(2))
    print(menu.__sum__())
    menu.__setIntem__(0, 'b')
    menu.__setIntem__(1, 'o')
    menu.__setIntem__(2, 'n')
    menu.__setIntem__(3, 'i')
    menu.__setIntem__(4, ' bb')
    print(menu.__sum__())