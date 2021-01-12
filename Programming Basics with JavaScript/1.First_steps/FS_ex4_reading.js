function reading(input) {
    let pagesToRead = Number(input[0]);
    let pagesHour = Number(input[1]);
    let allDays = Number(input[2]);

    let pagesPerDay = (pagesToRead / allDays) / pagesHour

    console.log(pagesPerDay)

}
reading(["212", "20", "2"])