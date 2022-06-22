arr = [1,0,2,3,0,4,5,0]
arr2 = [1,2,3]


def duplicate_zeros_1(arr):

    jump_iteration = False
    for i in range(0, len(arr) - 1):
        print(i)
        if arr[i] == 0 and (not jump_iteration):
            for j in range( len(arr)-2, i, -1):
                arr[j+1] = arr[j]
            arr[i+1] = 0
            jump_iteration = True
        else:
            jump_iteration = False
    return arr


def duplicate_zeros_2(arr):

    jump_iteration = False
    for i in range(0, len(arr) - 1):

        if jump_iteration:
            jump_iteration = not jump_iteration
            continue

        if arr[i] == 0:
            for j in range( len(arr)-2, i, -1):
                arr[j+1] = arr[j]
            arr[i+1] = 0
            jump_iteration = True
        
    return arr

if __name__=="__main__":
    print( duplicate_zeros_2(arr) )
    print( duplicate_zeros_2(arr2) )