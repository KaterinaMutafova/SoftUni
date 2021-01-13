function seconds(input) {
    first_player = Number(input[0]);
    second_player = Number(input[1]);
    third_player = Number(input[2]);

    let all_seconds = first_player + second_player + third_player;
    let minutes  =  Math.trunc(all_seconds / 60);
    let seconds = all_seconds % 60;

    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`);
    } else {
        console.log(`${minutes}:${seconds}`);
    }


}
seconds(["35", "45", "44"]);
seconds(["22", "7", "34"]);
seconds(["50", "50", "49"]);
seconds(["14", "12", "10"]);
