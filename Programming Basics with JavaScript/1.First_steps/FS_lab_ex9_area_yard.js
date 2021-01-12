function yard(area) {
    let yardArea = Number(area);
    let pricePerSqm = 7.61;
    let finalPrice = pricePerSqm * yardArea;
    let discount = finalPrice * 0.18;
    let finalfinalPrice = finalPrice - discount;

    console.log(`The  final price is: ${finalfinalPrice} lv.`);
    console.log(`The  discount is: ${discount} lv.`);


}
yard("550")