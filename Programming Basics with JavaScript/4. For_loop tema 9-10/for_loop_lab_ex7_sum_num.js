function sumNumbers(input) {
    let number = input[0];
    let sumDigits = 0
    for (let i = 0; i < number.length; i++) {
        sumDigits += Number(number[i]);


    }
    console.log(`The sum of the digits is:${sumDigits}`)


}

sumNumbers(["1234"])
sumNumbers(["564891"])