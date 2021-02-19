function hundred(input) {
    let number = Number(input[0]);
    if (number >= -100 && number <=100 && number != 0 ){

        console.log("Yes")
    } else {
        console.log("No")
    }


}


hundred(["-25"])
hundred(["0"])
hundred(["25"])