function leapYear(input) {
    let firstYear = Number(input[0]);
    let lastYear = Number(input[1]);

    for (let start = firstYear; start <= lastYear; start+=4) {
        console.log(start);


    } 

}
leapYear(["1908", "1919"])
