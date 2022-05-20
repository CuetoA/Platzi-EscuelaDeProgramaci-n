"""
    Algorithmic complexity approximation to Big-O Notation
    here we have: 1000 + x + 2 x^2
    with lim to infinite: x^2 -> BigO
"""


    
def f(x):
    for i in range (1000):
        print('Fixed operation, always 1000')
    
    for i in range(x):
        print('Lineal operation, always depends on X')
    
    for i in range(x):
        for j in range(x):
            print('Operation one. Square operation, x^2')
            print('Operation two. Square operation, x^2')