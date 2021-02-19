function flowers(input) {
    let flower = input[0];
    let count = Number(input[1]);
    let budjet = Number(input[2]);
    let priceFlowers = 0;
    // Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"
    if (flower === "Roses") {
        priceFlowers = count * 5;
        
        if (count > 80) {
            priceFlowers = 0.90 * priceFlowers;
        }
    } else if (flower === "Dahlias") {
        priceFlowers = count * 3.8;

        if (count > 90) {
            priceFlowers = 0.85 * priceFlowers;
        }
    } else if (flower === "Tulips") {
        priceFlowers = count * 2.8;

        if (count > 80) {
            priceFlowers = 0.85 * priceFlowers;
        }

    } else if (flower === "Narcissus") {
        priceFlowers = count * 3;

        if (count < 120) {
            priceFlowers = 1.15 * priceFlowers;
        }

    } else if (flower === "Gladiolus") {
        priceFlowers = count * 2.5;
        if (count < 80) {
            priceFlowers = 1.20 * priceFlowers;
        }
    }

    if (priceFlowers <= budjet) {
        let diff = budjet - priceFlowers;
        console.log(`Hey, you have a great garden with ${count} ${flower} and ${diff.toFixed(2)} leva left.`);
    } else if (priceFlowers > budjet) {
        let diff = priceFlowers - budjet;
        console.log(`Not enough money, you need ${diff.toFixed(2)} leva more.`);
    }
    
}

flowers(["Roses", "55", "250"])
flowers(["Tulips", "88", "260"])
flowers(["Narcissus", "119", "360"])

