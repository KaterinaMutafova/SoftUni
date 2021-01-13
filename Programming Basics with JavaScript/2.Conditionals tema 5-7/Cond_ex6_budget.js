function kingKong(input) {
    let budget = Number(input[0]);
    let countStats = Number(input[1]);
    let oneStatCloth = Number(input[2]);

    let decor = budget * 0.10;
    let clothesStats = countStats * oneStatCloth;
    if (countStats > 150) {
        clothesStats -= clothesStats * 0.10;
    }
    let filmMoney = clothesStats + decor;
    let difference = Math.abs(filmMoney - budget);
    if (filmMoney > budget) {
        console.log("Not enough money!")
        console.log(`Wingard needs ${difference.toFixed(2)} leva more.`)
    } else if (budget >= filmMoney) {
        console.log("Action!")
        console.log(`Wingard starts filming with ${difference.toFixed(2)} leva left.`)
    }

}

kingKong(["20000", "120", "55.5"])
kingKong(["15437.62", "186", "57.99"])
kingKong(["9587.88", "222", "55.68"])
