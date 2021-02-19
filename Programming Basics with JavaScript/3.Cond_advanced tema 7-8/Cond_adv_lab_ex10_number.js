function number(input) {
    let number = Number(input[0]);
    if ((number < 100 || number > 200) && number != 0 ){

        console.log("invalid")
    } 


}

number(["150"])
number(["75"])
number(["220"])
number(["199"])