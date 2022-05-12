"""
    In order to analyse and understand this algorithm we have divided it in two parts:
    1.- We need a loop that iterates through the array
    2.- We need a loop which sort the last value of the array
    
    The first one was analyzed with a deck of cards, simulating the algorithm.
    The next one was infered by the first one
"""

# Sort the last value of the array
arr = [1, 11, 7, 4, 3, 2]
currentValue = arr[-1]
currentPosition = len(arr) -1
print()
while currentPosition > 0 and currentValue < arr[currentPosition - 1]:
    print(f'current value: {currentValue}')
    arr[currentPosition] = arr[currentPosition - 1]
    currentPosition -= 1
arr[currentPosition] = currentValue

print(f'finished \nArr: {arr}\n')


# Insertion Sort
for n in range(1, len(arr)): #
    currentPosition = n
    currentValue = arr[n]  
    print()
    while currentPosition > 0 and currentValue < arr[currentPosition - 1]:
        print(f'current value: {currentValue}')
        arr[currentPosition] = arr[currentPosition - 1]
        currentPosition -= 1
    arr[currentPosition] = currentValue