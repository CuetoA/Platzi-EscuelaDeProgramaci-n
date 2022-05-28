
def my_gen():

    n = 0
    print(f'{n} iteration')
    yield n


    n = 1
    print(f'{n} iteration')
    yield n


    n = 2
    print(f'{n} iteration')
    yield n


def my_gen_2():

    n = 0
    while True:
        n += 1
        print(f'{n} iteration')
        yield n



if __name__=="__main__":
    a = my_gen_2()

    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))