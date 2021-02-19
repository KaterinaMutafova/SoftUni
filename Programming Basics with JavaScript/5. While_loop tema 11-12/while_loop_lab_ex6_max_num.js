function maxNumber(input) {
    let index = 0;
    let maxNum = input[index];
    index++;
    let command = input[index]
    while (command !== "Stop") {
        let num = Number(command);
        if (num > maxNum) {
            maxNum = num;
        }
        command = input[index];
        index++

    }
    console.log(maxNum)



}

maxNumber(["100", "99", "80", "70", "Stop"])
maxNumber(["-10", "20", "-30", "Stop"])
maxNumber(["45", "-20", "7", "99", "Stop"])
maxNumber(["999", "Stop"])
maxNumber(["-1", "-2", "Stop"])





