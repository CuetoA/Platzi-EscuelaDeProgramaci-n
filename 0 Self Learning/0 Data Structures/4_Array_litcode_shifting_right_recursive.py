
def duplicateZeros(arr):

    if len(arr) == 1: return arr

    print(f'{arr}')
    i = 0
    while i <= (len(arr)-1) :
        if arr[i] == 0:            
            duplicateZeros(arr[i+1:])
            break
        else:
            i += 1



if __name__=="__main__":
    arri = [0,4,0,6,3,0,0,2,5]
    duplicateZeros(arri)