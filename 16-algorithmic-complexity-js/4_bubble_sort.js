
function bubble_sort(arr){

    let len = arr.length
    for (let i = 0; i < len; i++){
        for(let j = 0; j < len; j++){

            let current = arr[j];
            let next =arr[j + 1];
            if ( current > next){
                let temp    = current;
                arr[j]      = next;
                arr[j + 1]  = temp; 
            } // if

        } // for j
    } // for i
    
    return arr
} // bubble_sort

arr = [2,4,3,1,9,6,7,0]
console.log( bubble_sort( arr ) )