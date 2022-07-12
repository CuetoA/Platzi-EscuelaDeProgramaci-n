const data = {
    frontend: "Pablito",
    backend: "Chompi",
    design: "Scarlette",
}

// This let us parse to array as in python
const entries = Object.entries(data);
console.log(entries.length);
console.log(entries);

// This allow us to get values as in python
const values = Object.values(data);
console.log(values);

// Changing strings
const string = 'hello';
console.log(string.padStart(7, 'hi'));
console.log(string.padEnd(12, 'H'));