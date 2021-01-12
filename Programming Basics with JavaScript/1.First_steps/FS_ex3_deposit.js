function deposit(input) {
    let moneyStart = Number(input[0]);
    let periodDeposit = Number(input[1]);
    let percentYear = Number(input[2]) / 100;

    let moneyEnd = moneyStart + (periodDeposit * ((moneyStart * percentYear)/12));

    console.log(moneyEnd);

}
deposit(["200", "3", "5.7"])