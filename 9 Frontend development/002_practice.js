function button_click(){
    let height = document.getElementById('i_height').value;
    let character = document.getElementById('i_character').value;
    
    // console.log(`height: ${height}`);
    // console.log(`character: ${character}`);

    calculate_arr(height, character);
}

let calculate_arr = (height, character) => {

    for(let iter = 0; iter < height; iter ++){
        num_spaces = (height - iter) -1 ;
        num_char = (iter * 2) +1;

        let my_str = ` `.repeat(num_spaces) + `${character}`.repeat(num_char);
        console.log(my_str)
    }
}