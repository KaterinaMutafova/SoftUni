function bonusCalc(num) {
    let number = Number(num[0]);
    let bonusPoints = 0;

    if (number > 1000)  {
        bonusPoints = number * 0.10;
    } else if (number > 100 && number <= 1000){
        bonusPoints = number * 0.20;
    } else if (number <= 100) {
        bonusPoints = 5;
    }

    if (number % 2 === 0)  {
        bonusPoints += 1;
    } else if (number % 5 === 0) {
        bonusPoints += 2;
    }

    let allPoints = number + bonusPoints
    console.log(bonusPoints);
    console.log(allPoints)

}
bonusCalc(["15875"])

