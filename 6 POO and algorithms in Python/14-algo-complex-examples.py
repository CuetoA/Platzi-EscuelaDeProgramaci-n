import numpy as np

# O(1)
#   Always the same because it knows where is the index
food = ['chicken', 'beef', 'rice', 'donut']
def findByIndex(food, index):
    return food[index]

# O( log(n) )        
def binarySearch(arr, start, end, x):
 
    # Check base case
    if end >= start:
 
        middle = start + ((end - start) // 2)
 
        # Search at the middle
        if arr[middle] == x:
            return middle
 
        elif x < arr[middle]:
            # Search at the left
            return binarySearch(arr, start, middle-1, x)
 
        else:
            # Search at the right
            return binarySearch(arr, middle + 1, end, x)
 
    else:
        # Element is not present in the array
        return -1

# O(n)
#   It depends on how large the element is
def selectedFood(food):
    for objectFood in food:
        print(objectFood)

# O(n^2)
#   No matter what it will do n twice
array = np.array( [1,2,3,4,5] )
def bubbleSort(array):
    array2 = array.copy()
    for i in range( len(array2) ):
        for j in range( len(array2) - 1 ):
            if array2[j] > array2[j+1]:
                array2[j], array2[j+1] = array2[j+1], array2[j]
    return array2

if __name__ == "__main__":
    arr = [30, 40, 50, 60, 70, 80, 90, 100, 110]
    print( binarySearch(arr, 0, len(arr), 90) )
    print( binarySearch(arr, 0, len(arr), 95) )
    print( binarySearch(arr, 0, len(arr), 45) )
    print( binarySearch(arr, 0, len(arr), 30) )