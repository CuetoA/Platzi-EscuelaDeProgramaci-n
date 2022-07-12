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


// Async y Await
//      basically it waits for your answer
const helloWorld = (number) => {
    return new Promise((resolve, reject) => {
        console.log(` Inside promise of helloWorld no. ${number}`);

        (true)
        ? setTimeout(() => resolve(`Hello world no. ${number}`), 3000)
        : reject(new Error('Test Error'))
    })
};

const helloAsync = async (number) => {
    const hello = await helloWorld(number);
    console.log(hello)
}

helloAsync(1);  // This waits
helloWorld(2);  // This doesnt