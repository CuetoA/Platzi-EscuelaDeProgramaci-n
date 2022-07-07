num = [12, 345, 2, 6, 7896]
nums2 = [555,901,482,1771]

def evenNumberOfDigits(arr):
    
    counter = 0
    for value in arr:
        try:    
            value_str = str(value)
            length = len(value_str)
            itsPair = length % 2 == 0
            if itsPair:
                counter += 1

        except: 
            print('somthing went wrong with parsing')
    
    return counter


if __name__=="__main__":
    print( evenNumberOfDigits(num) )
    print( evenNumberOfDigits(nums2) )
       
