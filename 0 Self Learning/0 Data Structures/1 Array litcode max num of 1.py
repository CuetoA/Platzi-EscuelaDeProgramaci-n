input = [1,1,0,0,1,1,1]


def maxConsecutiveNumber(input):
    length = len(input)
    counter = 0
    maxV = 0

    for i in range(length):
        value = input[i]
        if value == 1:
            counter += 1
        if value == 0 or i == length-1:
            maxV = max([counter, maxV])
            counter = 0
    
    return maxV


if __name__=="__main__":
     print( maxConsecutiveNumber(input) )