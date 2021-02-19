function outfit(input) {
    let degrees = Number(input[0]);
    let daytime = input[1];
    let outfit = "Any";
    let shoes = "Some";

    switch (daytime) {
        case "Morning":
            if (degrees >= 10 && degrees <= 18) {
                outfit = "Sweatshirt";
                shoes = "Sneakers";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            } else if (drgrees > 18 && degrees <= 24) {
                outfit = "Shirt";
                shoes = "Moccasins";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            } else if (degrees >= 25) {
                outfit = "T-Shirt";
                shoes = "Sandals";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            }

        case "Afternoon":
            if (degrees >= 10 && degrees <= 18) {
                outfit = "Shirt";
                shoes = "Moccasins";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            } else if (degrees > 18 && degrees <= 24) {
                outfit = "T-Shirt";
                shoes = "Sandals";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            } else if (degrees >= 25) {
                outfit = "Swim Suit";
                shoes = "Barefoot";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            }
        case "Evening":
            if (degrees >= 10 && degrees <= 18) {
                outfit = "Shirt";
                shoes = "Moccasins";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            } else if (degrees > 18 && degrees <= 24) {
                outfit = "Shirt";
                shoes = "Moccasins";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            } else if (degrees >= 25) {
                outfit = "Shirt";
                shoes = "Moccasins";
                console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`); break;
            }

    }


}

outfit(["16", "Morning"])
outfit(["22", "Afternoon"])
outfit(["28", "Evening"])


