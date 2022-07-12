// Replace all
const string = "Javascript is marvelous and with Javascript we can create the future through it"
const repplacedString = string.replace("Javascript", "Python");
const repplacedString2 = string.replaceAll("Javascript", "Python");

console.log(string)
console.log(repplacedString)
console.log(repplacedString2)


// Privat method
class Message{
    show(a){
        console.log(a);
    };

    #privateMethod(b){
        console.log(b);
    };
}

const message = new Message();
message.show('This string');


// Promise anni
const promise1 = new Promise( (resolve, reject) => reject("1") );
const promise2 = new Promise( (resolve, reject) => resolve("2") );
const promise3 = new Promise( (resolve, reject) => resolve("3") );

Promise.any([promise1, promise2, promise3])     // returns the first one that resolves
    .then(response => console.log(response))


// let garbage collector to clean this element or object
class anyClass {
    constructor(element){
        this.ref = new WeakRef(element)
    }
}


// Operators
console.group("Operators")

let isTrue = true;
let isFalse = false;
console.log(isTrue && isFalse);

let isTrue2 = true;
let isFalse2 = false;
console.log(isTrue2 &&= isFalse2);

let isTrue3 = true;
let isFalse3 = false;
console.log(isTrue3 || isFalse3);

let isTrue4 = true;
let isFalse4 = false;
console.log(isTrue4 ||= isFalse4);

let isUndefined = undefined;
console.log(isUndefined ??= isFalse);
console.groupEnd();