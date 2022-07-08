var myname = "Andrés"

// this will prompt the name
console.log(myname)

// this will too because it is global
function test(){
    console.log(myname)
    var another = "PLatzi"
}

// This will not be prompted due is local
console.log(another)


// In local you can acces global, but in global you wont acces locals