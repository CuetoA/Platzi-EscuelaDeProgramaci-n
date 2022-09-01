// O(n)


function linear_search(arr, target){
    for (let i=0; i <= arr.length ; i++){
        if (target === arr[i]){
            return i
        }
    }
    return -1
}

arr = [1,2,3,4,5,6,7,8]
console.log( linear_search(arr, 6) )

arr = ['a', 'b', 'c', 'd', 'e']
console.log( linear_search(arr, 'd') )