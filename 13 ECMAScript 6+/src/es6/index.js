// OPTIONAL PARAMETERS
// -es6
function newFunction (name, age, country){
    var name = name || 'oscar';
    var age = age || 32;
    var country = country || 'MX';
    console.log(name, age, country);
}

// +es6
function newFunction2(name = "oscar", age = 23, country = "Mx"){
    console.log(name, age, country);
}

newFunction2();
newFunction2("Andrés", 23);


// SPLIT IN STRINGS
// -es6
let lorem = "I just want to split this thing \n" 
+ "another phrase";
// +es6
let lorem2 = `Another phrase we need 
another phrase`

console.log(lorem);
console.log(lorem2);


// VARIABLES IN OBJECTS
// -es6
let person = {
    'name': 'Andrés',
    'age': 32,
    'country': 'Mexico'
}
console.log(person.name, person.age)
// +es6
let {name, country} = person;
console.log(name, country);


// JOIN ARRAYS
// +es6
let team1 = ['Scarlette', 'Andrés'];
let team2 = ['Ceres', 'Boni'];
let new_team = ['Pablo', ...team1, ...team2]
console.log(new_team);


<<<<<<< HEAD
// LET AND VAR
=======
>>>>>>> 804a9c2860ecbb35e8b94b5c810fe1b10e8486ca
// +es6
{
    var globalVar = "Global variable";
}
{
    let globalLet = "Global Let"    // just inside scope
}
console.log(globalVar);     // avialable
console.log(globalLet);     // not avialable


<<<<<<< HEAD
// CONSTANT
=======
>>>>>>> 804a9c2860ecbb35e8b94b5c810fe1b10e8486ca
// +es6
const a = 'b'; // it cannot chenge from ecmascript6


<<<<<<< HEAD
// CREATE OBJECTS WITH VARIABLES
=======
>>>>>>> 804a9c2860ecbb35e8b94b5c810fe1b10e8486ca
// -es6
let name = "andres";
let age = 23;
obj = {name: name, age: age};
// +es6
obj2 = {name, age};
console.log(obj);
console.log(obj2);


<<<<<<< HEAD
// ARROW FUNCTIONS
=======
>>>>>>> 804a9c2860ecbb35e8b94b5c810fe1b10e8486ca
// -es6
let names = [
    {name: "Scarlette", age: 25},
    {name: "Andrés", age: 23}
]
let list_names = names.map( function(item){
    console.log(item.name);
})
// +es6
let list_names2 = names.map(item => console.log(item.name));
const arrow_f = (element1, element2) => {console.log(`${element1}  ${element2}`)}
const arrow_f2 = element => console.log(`${element}`)

arrow_f("Boni bb", 14);
arrow_f2('Print this');

<<<<<<< HEAD
// ARROW FUNCTIONS
=======

>>>>>>> 804a9c2860ecbb35e8b94b5c810fe1b10e8486ca
// +es6
const helloPromise = () =>{
    return new Promise((resolve, reject)=>{
        if(false){
            resolve('Hey!');
        }else{
            reject('Ups!');
        }
    })
}

helloPromise()
    .then(response => console.log(response))
    .then(() => console.log('void'))
    .catch(error => console.log(error));