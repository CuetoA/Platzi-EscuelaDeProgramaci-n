console.log(myName);

var myName = "Andrés";

/*
    In this example it will display undefined two times.
    The internal behavour of this is that myName doesn't exists so javascript does:
        myName = undefined
        instead of rasing a error or smthng
*/


hey();

function hey(){
    console.log("Hey its me")
}


// If we declarate a function before initializing it will be prompted propperly due they are processed before