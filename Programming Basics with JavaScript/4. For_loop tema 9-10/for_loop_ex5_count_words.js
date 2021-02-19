function countWords(input) {
    let alowwedWords = 10;
    let string_w = input[0];
    let length = string_w.length;
    let counter = 0

    for (let i = 0; i <= length; i++) {
        if (string_w[i] == " ") {
            counter += 1;
        }

    }
    counter += 1
    if (counter > 10) {

        console.log(`The message is too long to be send! Has ${counter} words.`)
    } else {
        console.log("The message was send successfully!")
    }
 
}

countWords(["This message has exactly eleven words. One more as it's allowed!"])
countWords(["This message has ten words and you can send it!"])
