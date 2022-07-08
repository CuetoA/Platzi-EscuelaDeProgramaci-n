// Declarative
//  Function has it own name
function miFunction(){
    return 3
}
miFunction(10,3);


// Expresion
//  Function has no name, just variable
var miFunction = function(a, b){
    return a + b;
}

miFunction(10,3);



function helloThere(name){
    console.log(`hello there ${name}`)
}