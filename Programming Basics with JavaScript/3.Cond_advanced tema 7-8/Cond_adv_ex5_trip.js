function trip(input) {
    // Бюджета определя дестинацията, а сезона определя колко от бюджета ще изхарчи
    let budget = input[0];
    let season = input[1];
    let destination = "";
    let holidayType = "";
    let spentMoney = 0
    
    if (budget <= 100) {
        destination = "Bulgaria";
        if (season === "summer"){
           holidayType = "Camp"; 
           spentMoney = budget * 0.30


        } else if (season == "winter") {
            holidayType = "Hotel";
            spentMoney = budget * 0.70

        }

    } else if (budget > 100 && budget <= 1000)  {
        destination = "Balkans";
        if (season === "summer"){
            holidayType = "Camp"; 
            spentMoney = budget * 0.40
 
 
         } else if (season == "winter") {
             holidayType = "Hotel";
             spentMoney = budget * 0.80
 
         }

    } else if (budget > 1000) {
        destination = "Europe";
        holidayType = "Hotel";
        spentMoney = budget * 0.90

    }
    console.log(`Somewhere in ${destination}`)
    console.log(`${holidayType} - ${spentMoney.toFixed(2)}`)


}

trip(["50", "summer"])
trip(["75", "winter"])
trip(["312", "summer"])
trip(["678.53", "winter"])
trip(["1500", "summer"])


