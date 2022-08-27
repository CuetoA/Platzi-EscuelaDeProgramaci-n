// Page to check algorithmic complexity: https://radiant-anchorage-11930.herokuapp.com/
// TIME COMPLEXITY
// It depends on how many interactions the algorithm will do per each n increase
// In js we will see two options to check time performance.now() and console.time(End)('text')

require('perf_hooks')

function count(n){
    for (let index = 0; index < n; index++){
        const element = index;
        console.log(element)
    }
}

console.time('duration');
count(5);
console.timeEnd('duration');
