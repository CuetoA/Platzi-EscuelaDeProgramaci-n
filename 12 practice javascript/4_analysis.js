const salariesMex = mexico.map((person)=>{
    return person.salary;
});

const salariesMex_sorted = salariesMex.sort((salaryA, salaryB)=>{
    return salaryA - salaryB;
});

const median = getAverage(salariesMex);
console.log(`The median is: ${median}`);

const number = Math.ceil(salariesMex_sorted.length * 0.1);
const start = salariesMex.length - number
const salaryTop10 = salariesMex_sorted.splice(start, number);
const averageTop10 = getAverage(salaryTop10);
console.log(`Top 10 average is: ${averageTop10}`);




function getAverage(myList){
    var listSum = myList.reduce((acumulated = 0, newElement) => {return acumulated + newElement;})
    const average = listSum / myList.length;
    return average    
}