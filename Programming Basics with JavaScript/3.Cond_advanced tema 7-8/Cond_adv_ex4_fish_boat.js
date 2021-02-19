function fishBoat(input) {
    let budget = input[0];
    let season = input[1];
    let countFishermen = input[2];

    let rentBoat = 0;

    switch (season) {
        case "Spring": 
            rentBoat = 3000; break;

        case "Summer":
            rentBoat = 4200; break;

        case "Autumn":
            rentBoat = 4200; break;

        case "Winter":
            rentBoat = 2600; break;
    }

    if (countFishermen <= 6) {
        rentBoat = rentBoat * 0.90
        
    } else if (countFishermen >= 7 && countFishermen <= 11) {
        rentBoat = rentBoat * 0.85

    } else if (countFishermen >= 12) {
        rentBoat = rentBoat * 0.75 
        
    }
    if (countFishermen % 2 === 0 && season != "Autumn") {
        rentBoat = rentBoat * 0.95
        
    }

    
    if (budget >= rentBoat) {
        let difference = budget - rentBoat
        console.log(`Yes! You have ${difference.toFixed(2)} leva left.`)
    } else if (budget < rentBoat) {
        let difference = rentBoat - budget
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva.`)
    }



}


fishBoat(["3000", "Summer", "11"])
fishBoat(["3600", "Autumn", "6"])
fishBoat(["2000", "Winter", "13"])



