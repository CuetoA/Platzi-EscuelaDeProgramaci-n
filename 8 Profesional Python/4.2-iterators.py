


class EvenNumbers:
    """
        Gets all even numbers instead of storing them in memory
    """

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    num = EvenNumbers(1000)

    print(iter(num))
    print(next(num))
    print(next(num))