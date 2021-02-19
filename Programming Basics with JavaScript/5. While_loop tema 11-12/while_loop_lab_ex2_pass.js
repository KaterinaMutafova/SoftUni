function password(input) {
    let index = 0
    let name  = input[index];
    index++
    let password = input[index];
    index++
    let passToValidate = "";

    while (passToValidate != password) {
        passToValidate = input[index]
        index++

    }
    if (passToValidate == password) {
        console.log(`Welcome ${name}!`)
    }




}

password(["Nakov", "1234", "Pass", "1324", "1234"])
