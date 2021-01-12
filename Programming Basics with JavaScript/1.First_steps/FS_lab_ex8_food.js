function foodAnymals(dogs, otherAnimals){
    let dogNum = Number(dogs);
    let other = Number(otherAnimals);
    let priceDogFood = 2.5;
    let priceOtherFood = 4;

    let allSum = (dogNum * priceDogFood) + (other * priceOtherFood);
    console.log(`${allSum} lv.`);


}
foodAnymals("5", "4");