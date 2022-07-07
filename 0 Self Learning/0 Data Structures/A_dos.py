
def duplicateZeros(arr, shift_counter=0, end_p = 0):
    arr_size = len(arr)

    not_len_enough = (arr_size == 0)
    not_worth_operation = shift_counter > arr_size
    if  not_len_enough or not_worth_operation: return arr, arr_size - end_p

    print(f's: {shift_counter} \t\t arr: {arr}')
    i = 0
    while i <= (arr_size-2):
        if arr[i] == 0:
            arr[i+1:], end_p = duplicateZeros(arr[i+1:], shift_counter + 1, end_p)
            print(f's: {shift_counter} \t\t arr: {arr}')

            break
        else:
            i += 1
    
    if shift_counter > 0:
        for j in range(arr_size - end_p, shift_counter-1, -1):
            arr[j] = arr[j-shift_counter]
        arr[shift_counter-1] = 0
        end_p = arr_size - (shift_counter-2)
    print(f's: {shift_counter} \t\t arr: {arr}')

    return arr, end_p
    
    





if __name__=="__main__":
    arr1 = [0,4,0,6,3,0,2,5,4,6,7]
    arr2 = [1,2,3,0,4,5,6]
    arr3 = [0,1,2,0,4,5,6,0,7,8,0,10,11,13,0,14]
    arr4 = [1,2,3,4,5,0,6]
    arr5 = [1,0,2,3,0,4,5,0]
    arr6 = [8,4,5,0,0,0,0,7]
    arr7 = [0,1,7,6,0,2,0,7]

    arr = arr6
    print(f'input: \t\t {arr}')
    print(f'\nresultado: \t {duplicateZeros(arr)[0]}')