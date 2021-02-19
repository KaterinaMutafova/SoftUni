function sumNums (input) {
    let index = 0
    let boundarySum = Number(input[index]);
    index++
    let sumNumbers = 0
    while (sumNumbers < boundarySum) {
        sumNumbers += Number(input[index]);
        index++
    }
    console.log(sumNumbers)


}


sumNums(["100", "10", "20", "30", "40"])
sumNums(["20", "1", "2", "3", "4", "5", "6"])

