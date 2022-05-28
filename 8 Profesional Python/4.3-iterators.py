

class FibonacciIter():

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):

        if self.n2 >=self.limit:
            raise StopIteration

        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux


if __name__ == "__main__":
    fibonacci = FibonacciIter(10)
    iter(fibonacci)

    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))

    for elemento in fibonacci:
        print(elemento)

