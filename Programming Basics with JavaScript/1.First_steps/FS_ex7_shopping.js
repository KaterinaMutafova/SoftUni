function shopping(sPrice, bananas, oranges, raspberries, strawberies) {
    let strawberryPrice = Number(sPrice);
    let raspberryPrice = (1/2) * strawberryPrice; 
    let orangePrice = raspberryPrice - raspberryPrice * 0.40;
    let bananaPrice = raspberryPrice - raspberryPrice * 0.80;
    let bananaKg = Number(bananas);
    let orangesKg = Number(oranges);
    let raspberryKg = Number(raspberries);
    let strawberryKg = Number(strawberies);

    let allPrice = strawberryKg * strawberryPrice + orangesKg * orangePrice + bananaKg * bananaPrice + raspberryKg * raspberryPrice;

    console.log(allPrice);

}
shopping("48", "10", "3.3", "6.5", "1.7")