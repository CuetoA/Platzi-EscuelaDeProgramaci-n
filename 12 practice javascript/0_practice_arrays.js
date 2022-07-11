myarr = [1,2,3,4,5,6,7,8,9,10];
const mayarr_element = document.getElementById("show_arr");
mayarr_element.innerHTML = `My array is: ${myarr}`;


const my_map = myarr.map(element => { return element });
const my_map_el = document.getElementById("show_map");
my_map_el.innerHTML = `This is what a simple map looks like: ${my_map}`;    


const my_map2 = myarr.map(element => { return element * 5 });
const my_map_el2 = document.getElementById("show_map2");
my_map_el2.innerHTML = `We can operate in it like this ${my_map2}`;    


const my_reduce_el = document.getElementById("show_reduce");
my_reduce_el.innerHTML = `Reduce iterates through an object and recieves: 
    peviousValue, currentValue, currentIndex and the array. It starts at element 1 to get a prevoiusValue.
    Basically you just give them a function saying what you want to do with this elements, but how to iterate
    doesn't really matter. Example in console.
`;    
const my_reduce = myarr.reduce((previousValue, currentValue, currentIndex, array)=>{
    console.group(`${currentIndex} 1teration`)
    console.log(previousValue);
    console.log(currentValue);
    console.log(currentIndex);
    console.log(array);
    console.groupEnd();
})