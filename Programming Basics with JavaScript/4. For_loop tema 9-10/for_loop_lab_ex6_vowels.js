function vowels(input) {
    let word = input[0];
    let vowelsSum = 0;
    for (let i = 0; i < word.length; i++) {
        if (word[i] === "a") {
            vowelsSum += 1;
        } else  if (word[i] === "e") {
            vowelsSum += 2;
        } else if (word[i] === "i") {
            vowelsSum += 3;
        } else if (word[i] === "o") {
            vowelsSum += 4;
        } else if (word[i] === "u") {
            vowelsSum += 5;
        }

    }
    console.log(vowelsSum)




}

vowels(["hello"])
vowels(["hi"])
vowels(["bamboo"])