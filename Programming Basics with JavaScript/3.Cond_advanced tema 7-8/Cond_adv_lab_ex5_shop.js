function shop(input) {
    let product = input[0];
    let town = input[1];
    let quantity = Number(input[2]);
    let price = 0
    switch (town) {
        case "Sofia":
        if (product == "coffee"){
            price = quantity * 0.5;
            console.log(price);
        } else if (product == "water") {
            price = quantity * 0.8;
            console.log(price);
        } else if (product == "beer") {
            price = quantity * 1.2;
            console.log(price);
        } else if (product == "sweets") {
            price = quantity * 1.45;
            console.log(price);
        } else if (product == "peanuts") {
            price = quantity * 1.60;
            console.log(price);
        } break;

        case "Plovdiv":
        if (product == "coffee"){
            price = quantity * 0.4;
            console.log(price);
        } else if (product == "water") {
            price = quantity * 0.7;
            console.log(price);
        } else if (product == "beer") {
            price = quantity * 1.15;
            console.log(price);
        } else if (product == "sweets") {
            price = quantity * 1.30;
            console.log(price);
        } else if (product == "peanuts") {
            price = quantity * 1.50;
            console.log(price);
        } break;


        case "Varna":
        if (product == "coffee"){
            price = quantity * 0.45;
            console.log(price);
        } else if (product == "water") {
            price = quantity * 0.7;
            console.log(price);
        } else if (product == "beer") {
            price = quantity * 1.1;
            console.log(price);
        } else if (product == "sweets") {
            price = quantity * 1.35;
            console.log(price);
        } else if (product == "peanuts") {
            price = quantity * 1.55;
            console.log(price);
        } break;


    }
    


}

// shop(["coffee", "Varna", "2"])
// shop(["peanuts", "Plovdiv", "1"])
shop(["beer", "Sofia", "6"])
// shop(["water", "Plovdiv", "3"])
// shop(["sweets", "Sofia", "2.23"])