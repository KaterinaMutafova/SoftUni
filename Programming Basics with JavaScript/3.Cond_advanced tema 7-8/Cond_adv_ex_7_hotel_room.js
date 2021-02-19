function hotelRoom(input) {
    let month = input[0];
    let nights = Number(input[1]);
    let priceApertment = 0;
    let priceStudio = 0;

    if (month === "May" || month === "October") {
        if (nights > 14) {
            priceStudio = 50 * nights * 0.70;
            priceApertment = 65 * nights * 0.90;

        } else if (nights > 7) {
            priceStudio = 50 * nights * 0.95;
            priceApertment = 65 * nights; 
            
    
        } else {
            priceStudio = 50 * nights;
            priceApertment = 65 * nights; 
        }

    } else  if (month === "June" || month === "September") {
        if (nights > 14) {
            priceStudio = 75.20 * nights * 0.80;
            priceApertment = 68.70 * nights * 0.90;
        } else { 
            priceStudio = 75.20 * nights;
            priceApertment = 68.70 * nights;
        }

    } else if (month === "July" || month === "August") {
        if (nights > 14) {
            priceApertment = 77 * nights * 0.90;
            priceStudio = 76 * nights;

        } else {
            priceStudio = 76 * nights;
            priceApertment = 77 * nights;
        }
    }
    console.log(`Apartment: ${priceApertment.toFixed(2)} lv.`)
    console.log(`Studio: ${priceStudio.toFixed(2)} lv.`)




}

hotelRoom(["May", "15"])
hotelRoom(["June", "14"])
hotelRoom(["August", "20"])


