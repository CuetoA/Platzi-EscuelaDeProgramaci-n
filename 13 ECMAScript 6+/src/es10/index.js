// Flatten arrays
let array = [1, 2, 3, [1, 2, 3, [1, 2, 3]]];

console.log(array.flat())
console.log(array.flat(1))
console.log(array.flat(2))

// Map it while flatting
let other_arr = [1,2,3,4,5];
console.log(other_arr.flatMap( (value) => [value, value * 2]));

// Erase spaces from string
let hello = "             hello there          ";
console.log(hello + "...marker");
console.log(hello.trimStart() + "...marker");
console.log(hello.trimEnd() + "...marker");
console.log(hello.trim() + "...marker");


// Simplify try catch
try{

}catch{
    error
}

// Objects from arrays
let entries = [["name", "andres"], ["age", "23"]];
console.log(Object.fromEntries(entries));

//
let mySimbol = "MySimbol";
let symbol = Symbol(mySimbol);
console.log(symbol.description);