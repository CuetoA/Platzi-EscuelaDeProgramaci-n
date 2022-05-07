"""
Algorithmic complexity:
    It can be:
        - Spacial (memory)
        - Time

    ways to measure:
    - Time the algorithms is not the best way due its dependecy on software and hardware use
    - Count steps as abstract measurement. Its problem is that it could vary
    - Counting steps aproximating the dataset to the infinite
    
    Excercise with factorial:
"""

import time

def factorial(n):
    answer = 1
    
    while n >1:
            answer *= n
            n -= 1
            
    return answer


def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r( n-1 )

def timeTestF(fnc, n):
    print()
    startTime = time.time()
    fnc(n)
    endTime = time.time()
    duration = endTime - startTime
    print(f'Tardamos {duration} in executing the function \n')

if __name__ == '__main__':
    n =900
    
    # startTime = time.time()
    # print( factorial(n) )
    # endTime = time.time()
    # duration = endTime - startTime
    # print('Tardamos {final - comienzo}')
    
    timeTestF(factorial, n)
    timeTestF(factorial_r, n)
    
"""
    Iterating with larger numbers and may times we would see that this measurement is super innestabel
    Therefore, time is not the best way to compute eficency
"""