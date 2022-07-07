// alert('Hello there');

const name = "Andrés Cueto Estrada";
var height = 1.79;
const id = document.getElementById('test');
id.innerHTML = name;

id.innerHTML += `
    <h1>holiwis</h1>
    <p>
        My name is: ${name} and I am ${height} tall
    </p>
`

if(height >= 1.8){
    id.innerHTML+=`<p>${name} is tall!</p>`
}
else{
    id.innerHTML+=`<p>${name} is not tall!</p>`
}



MuestraMiNombre()

function MuestraMiNombre(){
    for(var i = 0; i<=5; i++){
        const app = document.getElementById('test');
        const header = document.createElement('p');
        const headerConent = document.createTextNode('${i}');
        header.appendChild(headerConent);
        app.appendChild(header);
    }
}


var names = ['Scarlette', 'Ceres', 'More']

for(i = 0; i< names.length; i++){
    var new_name = names[i]
    id.innerHTML+=`<p>${new_name}</p>`   
};


names.forEach((s_name) =>{
    id.innerHTML+=`<p> other ${s_name}</p>` 
});