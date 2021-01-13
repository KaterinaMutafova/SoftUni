function excursionCalc(input) {
    let pricePuzzle = 2.60;
    let priceDoll = 3;
    let priceBear = 4.10;
    let priceMinion = 8.20;
    let priceTruck = 2;

    let tripMoney = Number(input[0]);
    let puzzles = Number(input[1]);
    let dolls = Number(input[2]);
    let bears = Number(input[3]);
    let minions = Number(input[4]);
    let trucks = Number(input[5]);

    let allGain = puzzles * pricePuzzle + dolls * priceDoll + bears * priceBear + minions * priceMinion + trucks * priceTruck;
    let allToys = puzzles + dolls + bears + minions + trucks;

    if (allToys >= 50) {
        allGain = allGain * 0.75;
    }

    let rent = 0.10 * allGain;
    allGain = allGain - rent;

    let leftMoney = allGain - tripMoney;
    let neededMoney = tripMoney - allGain;

    if (allGain >= tripMoney) {
        console.log(`Yes! ${leftMoney.toFixed(2)} lv left.`);
    } else if (allGain < tripMoney) {
        console.log(`Not enough money! ${neededMoney.toFixed(2)} lv needed.`);
    }


}

excursionCalc(["40.8", "20", "25", "30", "50", "10"])
excursionCalc("320", "8", "2", "5", "5", "1")