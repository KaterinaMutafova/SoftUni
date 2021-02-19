function coins(input) {
    //  coins 2lv, 1lv, 0.50st, 0.20st, 0.10st, 0.05st, 0.02st, 0.01st
    let countCoins = 0;
    
    let change = Number(input[0]);

    change = change * 100;

    while(true) {
        countCoins += 1

        if (change >= 200) {
            change -= 200;
        } else if (change >= 100) {
            change -= 100;
        } else if (change >= 50) {
            change -= 50;
        } else if (change >= 20) {
            change -= 20;
        } else if (change >= 10) {
            change -= 10;
        } else if (change >= 5) {
            change -= 5;
        } else if (change >=2) {
            change -= 2;
        } else if (change >=1) {
            change -= 1;
        }

        if (change < 1) {
            break;
        }

    }

    console.log(countCoins)
    

}

coins(["1.23"])
coins(["2"])
coins(["0.56"])
coins(["2.73"])