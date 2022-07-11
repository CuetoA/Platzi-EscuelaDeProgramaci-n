const hello = () =>{
    return "Hello module!"
}

const bye = () => {
    return "Goodby my dear friend";
}

//export default hello;
module.exports = {hello, bye};