// Functions
function getFood(isFood){
    const promise = new Promise((resolve, reject) => {
        console.log(`isFood: ${isFood}`);
        
        // Ternary if
        (isFood)
        ? resolve("Burger") 
        : reject ( "We don't have that food")
    })
    return promise
}

const getFoodContainer = (isFood) => {getFood(isFood)
    .then(food => console.log(`Food is ${food}`))
    .catch(error => console.log(`Error is ${error}`))};


getFoodContainer(1);
getFoodContainer(0);