
def duplicateZeros(arr, s=0):

    if len(arr) == 1 or s>= len(arr): return arr

    print(f's={s} \t arr={arr}')
    i = 0
    while i <= (len(arr)-1) :
        if arr[i] == 0:
            s += 1         
            duplicateZeros(arr[i+1:], s)
            break
        else:
            i += 1



if __name__=="__main__":
    arri = [0,4,0,6,3,0,0,2,5]
    duplicateZeros(arri)