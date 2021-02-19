function devidedByNine(input) {
    let numberOne = Number(input[0]);
    let numberTwo = Number(input[1]);
    let sumNums = 0
    for (let i = numberOne; i <= numberTwo; i++) {
        if (i % 9 === 0) {
            sumNums += i;
        }
        
    }
    console.log(`The sum: ${sumNums}`);

    for (let i = numberOne; i <= numberTwo; i++) {
        if (i % 9 === 0) {
            console.log(i);
        }
        
    }


}

devidedByNine(["100", "200"])