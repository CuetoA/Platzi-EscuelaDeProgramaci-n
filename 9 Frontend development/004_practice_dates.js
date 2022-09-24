console.log('Hello there');

let time = Date.now();
console.log('Times type in ms: ', time);

let date = new Date();
console.log('New Date: ', date);

date = new Date(2022, 8, 21);   // Year, month -1, day
console.log('New selected Date: ', date);

date = new Date(1998, 7 - 1, 27);   // Year, month -1, day
console.log('My birthday: ', date);

date = new Date(1996, 11 - 1, 18);   // Year, month -1, day
console.log('Scarlettes birthday: ', date);

date = new Date(2018, 10 - 1, 14);   // Year, month -1, day
console.log('The day we started: ', date);

let today = new Date();
let today_m = today.getMonth();
let today_d = today.getDate();
let aniv = new Date(2018, 10 - 1, 14);
let aniv_m = aniv.getMonth();
let aniv_d = aniv.getDate();


let is_aniv = ( today_m == aniv_m ) && ( today_d == aniv_d )

    is_aniv ? console.log('todays is your aniversary') : console.log('today is not your aniversary')

