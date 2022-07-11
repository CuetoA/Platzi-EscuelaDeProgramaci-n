existingCupons = {
    1234567: 10,
    7654321: 30,
    1111222: 50,
    2222111: 70,
}


function calculatePrice(originalPrice, discount){
    const realPercentage = 100 - discount;
    const finalPrice = originalPrice * realPercentage / 100;
    return finalPrice
}

function onclickprice(){
    const price = document.getElementById("price").value;
    const cupon = document.getElementById("cupon").value;

    const discount = existingCupons[cupon];
    if (discount){
        const finalprice = calculatePrice(price, discount);
        message = `Final price is: ${finalprice}`;
    }else{
        message = "There is no discount"
    }

    const finalPriceElement = document.getElementById("finalprice");
    finalPriceElement.innerHTML = message;
    
}


// console.log({
//     originalPrice,
//     discount, 
//     realPercentage,
//     finalPrice
// })