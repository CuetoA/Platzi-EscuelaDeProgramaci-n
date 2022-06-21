num = [12, 345, 2, 6, 7896]
nums2 = [555,901,482,1771]

def evenNumberOfDigits(nums):
    
    counter = 0
    for i in range( len( nums ) ):
        if len( str( nums[i] ) ) % 2 == 0:
            counter += 1

    return counter


if __name__=="__main__":
    print( evenNumberOfDigits(num) )
    print( evenNumberOfDigits(nums2) )
       