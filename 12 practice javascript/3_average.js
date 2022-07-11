
// Code
const myList = [1,1,1,2,2,2,3,3,2,1,2,3,5,4,7,8,5,6,7,8,54,3];
const element = document.getElementById("array");
element.innerHTML = `The array is: [${myList}]`;

const average = getAverage(myList);
const element1 = document.getElementById("average_result");
element1.innerHTML = `The average is: ${average}`;

const median = getMedian(myList);
const element2 = document.getElementById("median_result");
element2.innerHTML = `The median is: ${median}`


const mode = getMode(myList);
const element3 = document.getElementById("mode_result");
element3.innerHTML = `The mode is: ${mode}`

// Functions
function getAverage(myList){
    var listSum = myList.reduce((acumulated = 0, newElement) => {return acumulated + newElement;})
    const average = listSum / myList.length;
    return average    
}

function getMedian(myList){
    myList = myList.sort();
    const list_size = myList.length;
    const is_odd = list_size % 2;

    if (is_odd){
        var position = Math.ceil(list_size / 2) - 1;
        return myList[position]
    }else{
        var positionR = (list_size / 2);
        var positionL = (list_size / 2)-1;
        let median = (myList[positionR] - myList[positionL])/2 + myList[positionL]
        return median
    }
    
}


function getMode(myList){
    counterList = {};
    myList.map((element)=>{
        if (counterList[element]){
            counterList[element] += 1;
        }else{
            counterList[element] = 1;
        }
    })

    var sortedList = Object.entries(counterList).sort((A, B) => {
        return A[1] - B[1];
    })
    
    return  sortedList.pop()[0]
}