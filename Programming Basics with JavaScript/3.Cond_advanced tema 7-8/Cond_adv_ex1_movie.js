function movie(input) {
    let type = input[0];
    let rows = Number(input[1]);
    let columns = Number(input[2]);
    let price = 0;
    switch (type) {
        case "Premiere":
            price = 12;
            income = rows * columns * price
            console.log(`${income.toFixed(2)} leva`); break;

        case "Normal":
            price = 7.50;
            income = rows * columns * price
            console.log(`${income.toFixed(2)} leva`); break;

        case "Discount":
            price = 5;
            income = rows * columns * price
            console.log(`${income.toFixed(2)} leva`); break;

    }

}

movie(["Premiere", "10", "12"])
movie(["Normal","21", "13"])


