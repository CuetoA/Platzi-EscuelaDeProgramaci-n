""" 
Binary search function.

- Iterative approach - meaning using loops.
- Fastest

i/o
- i: list, value
- o: index or -1

resructions:
- integers
- sorted increasingly
- non repited
- positive and negative
- no range
"""

def binary_search(input_array, value):
    """Your code goes here."""

    start = 0
    end = len(input_array)
    l   = len(input_array)

    while True:
        i = start + (end - start)//2
        print(f"i is {i}")

        if i+1 < start  or  i >= end:
            return -1

        if input_array[i] == value:
            return i

        bigger = value > input_array[i]
        if bigger:  start   = i + 1
        else:       end     = i -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print( binary_search(test_list, test_val2) )
print( binary_search(test_list, test_val1) )