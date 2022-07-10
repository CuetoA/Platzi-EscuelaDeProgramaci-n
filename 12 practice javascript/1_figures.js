console.log("Helo js")



// API functions
function get_square_perimeter(){
    const element = document.getElementById("square_input");
    const value = element.value;
    const perimeter = square_perimeter(value);
    alert(`The square perimeter is: ${perimeter}`)
}

function get_square_area(){
    const element = document.getElementById("square_input");
    const value = element.value;
    const area = square_area(value);
    alert(`The square area is: ${area}`)
}











// Sqare
function square_measurements(side_1){
    console.group("Sqare");
    console.log(`The sides of our sqare are ${side_1} cm`);
    square_perimeter(side_1);
    square_area(side_1);
    console.groupEnd();
}

function square_area(side_1){
    var area = side_1 * side_1;
    console.log(`The area is ${area} cm²`);
    return area
}

function square_perimeter(side_1){
    var perimeter = side_1 * 4;
    console.log(`The perimeter is ${perimeter} cm`);
    return perimeter
}



// Triangle
function triangle_measurements(side_1, side_2, side_3, base, height){
    console.group("Triangle");
    console.log(`The sides are: ${side_1}, ${side_2} and ${side_3}`);
    triangle_perimeter(side_1, side_2, side_3);
    triangle_area(base, height);
    console.groupEnd();
}

function triangle_perimeter(side_1, side_2, side_3){
    var triangle_perimeter = side_1 + side_2 + side_3;
    console.log(`The perimeter is ${triangle_perimeter} cm`);
    return triangle_perimeter    
}

function triangle_area(base, height){
    var triangle_area = base * height / 2;
    console.log(`The area is ${triangle_area} cm²`);
    return triangle_area
}

function verifyIsoseles(side_1, side_2, side_3){
    case1 = side_1 == side_2;
    case2 = side_2 == side_3;
    case3 = side_3 == side_1;
    var eq_sides, base;

    if (case1){
        eq_sides = side_1;
        base = side_3;
        return [base, eq_sides]
    }else if(case2){ 
        eq_sides = side_2;
        base = side_1;
        return [base, eq_sides]
    }else if(case3){
        eq_sides = side_3;
        base = side_2;
        return [base, eq_sides]
    }else{
        alert("It is not an isoceles")
        return undefined
    }
}

function calculateHeight(base, side){
    c = base/2;
    h = Math.sqrt(side**2 - c**2);
    return h
}
function calculateArea(base, height){
    const area = base * height / 2;
    alert(`The area is ${area}`);
    return 
}

function getIsocelesHight(){
    side_1 = document.getElementById("triangle_side1").value
    side_2 = document.getElementById("triangle_side2").value
    side_3 = document.getElementById("triangle_side3").value
    // sides = [side_1, side_2, side_3]
    const base_and_side = verifyIsoseles(side_1, side_2, side_3);
    if (Boolean(base_and_side)){
        const base = base_and_side[0]
        const side = base_and_side[1]
        console.log(`base: ${base} \t side: ${side}`)
        const height = calculateHeight(base, side);
        //alert(`The height is ${height}`)
        calculateArea(base_and_side[1], height);
    }
}


// Circle
function circle_measurements(radius){
    console.group("Circle");
    console.log(`Radius is ${radius}`);
    circle_perimeter(radius);
    circle_area(radius);
    console.groupEnd();
}

function circle_area(radius){
    const pi = Math.PI;
    var circle_area = pi * radius ** radius;
    console.log(`Area is ${circle_area} cm²`);
    return circle_area
}

function circle_perimeter(radius){
    const pi = Math.PI;
    var circle_perimeter = radius * 2 * pi;
    console.log(`Perimeter is ${circle_perimeter} cm`);
    return circle_perimeter
}


// Code
square_measurements(5, 6);
triangle_measurements(6, 7, 8, 6, 7);
circle_measurements(3);