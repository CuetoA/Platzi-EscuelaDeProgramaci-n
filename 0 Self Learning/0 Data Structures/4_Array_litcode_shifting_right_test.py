import random
import time

from A_uno import duplicate_zeros_2
from A_dos import duplicateZeros

def current_milli_time():
    return round(time.time() * 1000)

if __name__=="__main__":

    print('\nCreating array')
    nums =  [1,2,3,4,5,6,7,8,9,0,0,0,0]
    arr = []
    for i in range(4001):
        arr.append(random.choice(nums))
    arr2 = arr.copy()
    print('created array')
    print(f'Array len: {len(arr)}')
    # print(f'arr:           {arr}')

    print('\nRecursive:')
    s = current_milli_time()
    ans = duplicateZeros(arr)
    f = current_milli_time()
    print(f'executed time: {f-s} ms')
    # print(f'ans:           {ans[0]}')

    print('\nNormal:')
    s = current_milli_time()
    ans = duplicate_zeros_2(arr2)
    f = current_milli_time()
    print(f'executed time: {f-s} ms')
    # print(f'ans:           {ans}')


