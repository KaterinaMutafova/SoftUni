function birthday(input) {
    let rent = Number(input[0]);
    let cake  = 0.20 * rent;
    let drinks = cake - (0.45 * cake);
    let animator = (1 / 3) * rent
    let budget = rent + cake + drinks + animator

    console.log(budget)

}
birthday(["2250"])