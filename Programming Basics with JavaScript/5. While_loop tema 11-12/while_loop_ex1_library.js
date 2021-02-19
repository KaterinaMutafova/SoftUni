function library(input) {
    let index = 0;
    let searchedBook = input[index];
    let counter = 0
    index++;
    let book = input[index];
    let is_found = false;
    

    while (book != "No More Books") {
        let newBook = book;
        index++;
        if (book === searchedBook) {   
            is_found = true;
            break;

        } else {
            counter += 1
            book = input[index];
            
        }

    

    }

    if (is_found) {
        console.log(`You checked ${counter} books and found it.`);
    } else {
        console.log("The book you search is not here!")
        console.log(`You checked ${counter} books.`)
    }




}

library(["Troy", "Stronger", "Life Style", "Troy"])
library(["The Spot", "Hunger Games", "Harry Potter", "Torronto", "Spotify", "No More Books"])

