


def recursion(number):
    
    if number > 0:    
        number = recursion(number - 1)
    return number
    

if __name__ == "__main__":
    n = 5
    f1 = recursion(n)
    print(f'n: \t{n}')
    print(f'f1: \t{f1}')
    