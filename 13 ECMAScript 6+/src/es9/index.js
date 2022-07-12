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