"""
    Big-O notation
    
    Here we'll see some examples
"""

# Example 1
def f(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)
# O(n) + O(n) = O( n + n ) = O(2n) = O(n)


# Example 2
def f(n):
    for i in range(n):
        print(i)
    
    for j in range(n * n):
        print(j)
# O(n) + O(n * n) = O(n) + O(n^2) = O(n + n^2) = O(n^2) 


# Example 3
def f(n):
    for i in range(n):
        for j in range(n * n):
            print(j)
# O(n) * O(n * n) = O(n) * O(n^2) = O(n * n^2) = O(n^3) 


# Example 3
def f(n):
    for i in range(n):
        for j in range(n * n):
            print(j)
# O(n) * O(n * n) = O(n) * O(n^2) = O(n * n^2) = O(n^3)     


# Example 4
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
# 2 opetarions for each one
# Each operation creates 2 more
# Until n == 1 or 0
# :: O( 2^n )
