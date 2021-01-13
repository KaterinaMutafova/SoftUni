function plus(input) {
    let hour = Number(input[0]);
    let minute = Number(input[1]);
    let allMinutes = hour * 60 + minute;
    let timePlus = allMinutes + 15;
    let finalHour = Math.trunc(timePlus / 60);
    let finalMin = timePlus % 60;
    if (finalHour > 23) {
        finalHour = 0
    }

    if (finalMin < 10) {
        console.log(`${finalHour}:0${finalMin}`);
    } else {
        console.log(`${finalHour}:${finalMin}`);
    }


}
plus(["1", "46"]);
plus(["0", "01"]);
plus(["23", "59"]);
plus(["11", "08"]);
plus(["12", "49"]);