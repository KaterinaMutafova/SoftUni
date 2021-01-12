function charity(days, bakers, cakesPerBaker, gofrettesPerBaker, pancakesPerBaker) {
    let cakePrice = 45;
    let gofrettePrice = 5.80;
    let pancakePrice = 3.20;
    let daysNum = Number(days);
    let bakersNum = Number(bakers);
    let cakesNum = Number(cakesPerBaker);
    let gofretteNum = Number(gofrettesPerBaker);
    let pancakeNum = Number(pancakesPerBaker);

    let priceGoodsPerBaker = cakePrice * cakesNum + gofrettePrice * gofretteNum + pancakePrice * pancakeNum;

    let priceAllBakersPerDay = priceGoodsPerBaker * bakersNum;
    let priceAll = priceAllBakersPerDay * daysNum;
    let expense = (1 / 8) * priceAll;
    let finalsum = priceAll - expense;
    console.log(finalsum);

}
charity("23", "8", "14", "30", "16")