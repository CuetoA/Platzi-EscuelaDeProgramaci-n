
def duplicateZeros(arr, s=0, end_p = 1):

    if len(arr) == 1 or s>= len(arr): return arr, len(arr)

    print(f's={s} \t arr={arr}')
    i = 0
    while i <= (len(arr)-1) :
        if arr[i] == 0:
            #s += 1         
            arr[i+1:], end_p = duplicateZeros(arr[i+1:], s + 1, end_p)
            print(f's={s} \t arr={arr}')
            break
        else:
            i += 1
    
    # Hay que saber:
    #   Qué porción del arreglo realmente queremos modificar
    #   Comprobar que estamos modificando esa porción
    #   Realizar el corrimiento
    
    if s>0:
        for j in range(len(arr)-end_p, s-1, -1):
            arr[j] = str(arr[j-s])
        arr[s-1] = '0'
        #arr[s] = 0
        end_p = len(arr)


    # Original
    # for j in range(len(arr)-end_p, s-1, -1):
    #     arr[j] = arr[j-s]
    # arr[s-1] = 0
    # arr[s] = 0
    # end_p = len(arr) - s -1

    print(f's={s} \t arr={arr}')
    return arr, end_p
    
    





if __name__=="__main__":
    arr1 = [0,4,0,6,3,0,2,5,4,6,7]
    arr2 = [1,2,3,0,4,5,6]
    arr3 = [1,2,3,0,4,5,6,0,7,8,9]

    print(f'\nresultado: {duplicateZeros(arr3)}')