const mexico = [];

mexico.push(createPerson("Scarlette", 19000));
mexico.push(createPerson("Ceres", 24000));
mexico.push(createPerson("Andrés", 100));
mexico.push(createPerson("Boni", 500));
mexico.push(createPerson("Api", 50000));
mexico.push(createPerson("Guille", 5000));
mexico.push(createPerson("Lena", 30000));
mexico.push(createPerson("Luis", 14000));
mexico.push(createPerson("Trujis", 24000));
mexico.push(createPerson("Max", 30000));
mexico.push(createPerson("Rafa", 34000));






// Functions
function createPerson(name, salary){
    let person = {
        name: name,
        salary: salary
    }
    return person
}

