function record(input) {
    let worldRecordtime = input[0];
    let distance = input[1];
    let timePerMetre = input[2];

    let allTime = distance * timePerMetre;
    allTime  = Math.floor(distance / 15) * 12.5 + allTime;

    let difference = allTime - worldRecordtime;
    if (allTime > worldRecordtime) {
        console.log(`No, he failed! He was ${difference.toFixed(2)} seconds slower.`);
    }else if (allTime < worldRecordtime) {
        console.log(`Yes, he succeeded! The new world record is ${allTime.toFixed(2)} seconds.`);
    }

}

record(["10464", "1500", "20"])
record(["55555.67", "3017", "5.03"])