function smallest(input) {
    let countNum = Number(input[0]);

    let smallestNum = Number(input[1]);

    for (let i = 1; i <= countNum; i++) {
        let currentNum = Number(input[i]);
        if (currentNum < smallestNum) {
            smallestNum = currentNum;
        }

    }

    console.log(smallestNum);


}

smallest(["2", "100", "99"]);
smallest(["3", "10", "20", "-30"]);
smallest(["4", "45", "-20", "7", "99"]);


