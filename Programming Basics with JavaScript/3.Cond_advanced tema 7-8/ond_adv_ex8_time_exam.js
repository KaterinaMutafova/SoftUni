function time(input) {
    let hourExam = Number(input[0]);
    let minExam = Number(input[1]);
    let hourArrival = Number(input[2]);
    let minArrival = Number(input[3]);

    let totalMInExam = minExam + hourExam * 60;
    let totalMinArrival = minArrival + hourArrival * 60;
    let difference = Math.abs(totalMinArrival - totalMInExam)
    let hh = Math.trunc(difference / 60)
    let mm = difference % 60

    if (totalMinArrival < totalMInExam - 30) {
        console.log("Early")
        if (difference <= 59) {
            console.log(`${mm} minutes before the start`)

        } else if (difference > 59) {
            if (mm <= 9) {
                console.log(`${hh}:0${mm} hours before the start`)
            } else {
                console.log(`${hh}:${mm} hours before the start`)
            }
        }


    } else if (totalMinArrival >= totalMInExam - 30 && totalMinArrival <= totalMInExam ) {
        console.log("On time")
        if (totalMinArrival != totalMInExam) {
            console.log(`${mm} minutes before the start`)
        }

    } else if (totalMinArrival > totalMInExam) {
        console.log("Late")
        if (difference <= 59) {
            console.log(`${mm} minutes after the start`)

        } else if (difference > 59) {
            if (mm <= 9) {
                console.log(`${hh}:0${mm} hours after the start`)
            } else {
                console.log(`${hh}:${mm} hours after the start`)
            }
        }


    }

  


}

// time(["9", "30", "9", "50"])
// time(["9", "00", "10", "30"])
// time(["10", "00", "10", "00"])
// time(["9", "00", "8", "30"])
// time(["14", "00", "13", "55"])
// time(["11", "30", "10", "55"])
// time(["16", "00", "15", "00"])
// time(["11", "30", "8", "12"])
time(["11", "30","12", "29"])









