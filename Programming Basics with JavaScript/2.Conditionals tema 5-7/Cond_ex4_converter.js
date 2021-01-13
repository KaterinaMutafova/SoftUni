function conventer(input) {
    initialNum = Number(input[0]);
    initialParam = input[1];
    finalparam = input[2];
    finalNum = Number(input[0]);

    if (initialParam == "cm") {
        finalNum = initialNum / 100;
    } else  if (initialParam == "mm") {
        finalNum = initialNum / 1000;
    }

    if (finalparam == "mm") {
        finalNum = (finalNum * 1000).toFixed(3)
        console.log(finalNum)
    } else if (finalparam == "cm") {
        finalNum = (finalNum * 100).toFixed(3)
        console.log(finalNum)
    } else {
        console.log(finalNum.toFixed(3))
    }

}
converter(["12", "mm", "m"])
converter(["150", "m", "cm"])
converter(["45", "cm", "mm"])