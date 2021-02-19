function cake(input) {
    let cakeWidth = Number(input[0]);
    let cakeLength = Number(input[1]);
    let piecesCake = 0
    piecesCake = cakeWidth * cakeLength;
    let index = 0
    let command = input[2 + index];
    index++;

     while (command != "STOP") {
        let numberPieces = Number(command);
        piecesCake = piecesCake - numberPieces;
        if (piecesCake < 0) {
            console.log(`No more cake left! You need ${Math.abs(piecesCake)} pieces more.`)
            break;
        }
        command = input[2 + index];
        index++;

     }
     if (piecesCake > 0) {
         console.log(`${piecesCake} pieces are left.`)
     }


}

cake(["10", "10", "20", "20", "20", "20", "21"])
cake(["10", "2", "2", "4", "6", "STOP"])



