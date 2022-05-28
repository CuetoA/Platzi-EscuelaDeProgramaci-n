
def fibonacci_gen(limit):
    n1 = 0
    n2 = 1
    counter = 0
    lim = limit

    while True:
        if n2 >= lim:
            raise StopIteration(f'error {n2} >= {lim}')
        if counter == 0: 
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1 , n2 = n2, aux
            counter += 1
            yield aux


if __name__== "__main__":
    a = fibonacci_gen(10)

    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))

    while True:
        print(next(a))
