function forLoopDemo(input) {
    let ourNumber = Number(input[0]);

    for (let i = 1; i <= 10; i++) {

        console.log(`${i} * ${ourNumber} = ${i * ourNumber}`);
    }



}
forLoopDemo(['5'])