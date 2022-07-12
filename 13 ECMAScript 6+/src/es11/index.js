const button = document.getElementById("btn");

button.addEventListener("click", async () => {
    const module = await import("./file.js");
    module.hello()
});


// Big Integer
const aBigNumber = 9007199254740991n;
const anotherBigNumber = BigInt(9007199254740991);

// Promise All settled
const promise1 = new Promise( (resolve, reject) => reject("reject 1"));
const promise2 = new Promise( (resolve, reject) => resolve("reject 2"));
const promise3 = new Promise( (resolve, reject) => resolve("resolve 3"));

Promise.allSettled([promise1, promise2, promise2])  // waits for all the promises to finish no mater resolve or rejected
    .then(response => console.log(response))
    .catch(idk => console.log(idk))
    .finally( () => console.log('finished promises') );


// Global this
console.log(window);
console.log(globalThis);    // helps with acces from backend

// Null operator
const fooo = null ?? "default strung";  // will return the deffault
console.log(fooo)

const fooo2 = "another" ?? "default strung";    // will return the first value
console.log(fooo2)

// Optional something
const user = {};
console.log(user.profile.email)
console.log(user?.profile?.email);  // returns undefined without breaking the code

if(user?.profile?.email){
    console.log("then send email")
}else{
    console.log("email not found")
}