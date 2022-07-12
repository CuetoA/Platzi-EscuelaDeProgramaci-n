const hello = () =>{
    return "Hello module!"
}

const bye = () => {
    return "Goodby my dear friend";
}

//export default hello; <- es6
module.exports = {hello, bye};