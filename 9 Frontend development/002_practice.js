function button_click(){
    let height = document.getElementById('i_height').value;
    let character = document.getElementById('i_character').value;
    let my_text_el = document.getElementById('my_text');
    
    // console.log(`height: ${height}`);
    // console.log(`character: ${character}`);

    let my_str = calculate_arr(height, character);
    // my_text_el.innerHTML = my_str;
}

let calculate_arr = (height, character) => {
    
    var my_str = ''
    for(let iter = 0; iter < height; iter ++){
        num_spaces = (height - iter) -1 ;
        num_char = (iter * 2) + 1

        my_str += ` `.repeat(num_spaces) + `${character}`.repeat(num_char) + '\n';
    }

    console.log(my_str);
    return my_str
}