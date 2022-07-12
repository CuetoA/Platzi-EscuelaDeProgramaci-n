// OBJECT PROPERTIES EXTRACTION
const data = {
    name: "andres",
    age: 23,
    country: "Mx",
};

let {name, ...all} = data;   // Get all and name separated
console.log(name, all);
let {country, ...everything_elsed} = data; // Get all but country
console.log(everything_elsed);


// PROPAGATION
const obj = {
    name: "Scarlette",
    age: 24,
}

const obj1 = {
    ...obj,
    country: "Mx",
}

console.log(obj1)


// PROMISE.FINALLY
//      know when call has ended
const helloWorld = () => {
    return new Promise( (resolve, reject) => {
        (true)
        ? setTimeout( () => resolve("Hello there"), 3000)
        : reject("Godby there")
    });
};

helloWorld()
    .then(response => console.log(`Response is: ${response}`))
    .catch(error => console.log(`Error is: ${error}`))
    .finally(() => console.log("It has finished"));     // needs to be function