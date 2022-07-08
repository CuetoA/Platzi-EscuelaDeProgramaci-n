
var flag = "a";

function test(flag){
    if (flag === "a"){
        console.log(`flag is ${flag}`)
    }else if (flag){
        console.log(`flag exists and is ${flag}`)
    }else{
        console.log(`idk what is ${flag}`)
    }
}


// Ternary operator
// condition ? true_statement : false_statement
var condition = true;
condition ? console.log("it is true") : console.log("it is false")
var test_2 = condition ? "it is true" : "it is false"
console.log(test_2)