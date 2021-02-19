function numbersOperations(input) {
    let numberOne = Number(input[0]);
    let numberTwo = Number(input[1]);
    let operator = input[2];
    let result = 0
    let evenOdd = ""

    // "+", "-", "*", "/", "%"
    switch (operator) {
        case "+": 
        result = numberOne + numberTwo;
        if (result % 2 === 0) { 
            evenOdd  = "even"
        } else {
            evenOdd = "odd"
        }; 
        console.log(`${numberOne} ${operator} ${numberTwo} = ${result} - ${evenOdd}`); break;

        case "-": 
        result = numberOne - numberTwo; 
        if (result % 2 === 0) {
            evenOdd  = "even"
        } else {
            evenOdd = "odd"
        }; 
        console.log(`${numberOne} ${operator} ${numberTwo} = ${result} - ${evenOdd}`); break;

        case "*": 
        result = numberOne * numberTwo;
        if (result % 2 === 0) {
            evenOdd  = "even"
        } else {
            evenOdd = "odd"
        }; 
        console.log(`${numberOne} ${operator} ${numberTwo} = ${result} - ${evenOdd}`); break;

        case "/": 
        if (numberTwo === 0) {
            console.log(`Cannot divide ${numberOne} by zero`); break
        } else {
            result = numberOne / numberTwo; 
            console.log(`${numberOne} ${operator} ${numberTwo} = ${result.toFixed(2)}`); break;
        }
          
        case "%": 
        if (numberTwo === 0) {
            console.log(`Cannot divide ${numberOne} by zero`); break
        } else {
            result = numberOne % numberTwo; 
            console.log(`${numberOne} ${operator} ${numberTwo} = ${result}`); break;
        }


    }
   

}


numbersOperations(["10", "12", "+"])
numbersOperations(["10", "1", "-"])
numbersOperations(["7", "3", "*"])
numbersOperations(["123", "12", "/"])
numbersOperations(["10", "3", "%"])
numbersOperations(["112", "0", "/"])
numbersOperations(["10", "0", "%"])






