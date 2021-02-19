function moving(input) {
    let index = 0
    let width = Number(input[index]);
    index++;
    let length = Number(input[index]);
    index++;
    let height = Number(input[index]);
    index++;
    let volume = width * length * height;

    let command = input[index];
    
    while (command != "Done") {
        luggage = Number(command);
        index++;
        volume -= luggage;
        if (volume < 0) {
            let difference = Math.abs(volume);
            console.log(`No more free space! You need ${difference} Cubic meters more.`);
            break;
        } 

        command = input[index];

    }

    if (volume > 0) {
        console.log(`${volume} Cubic meters left.`);

    } 


}

moving(["10",  "10", "2", "20", "20", "20", "20", "122"])
moving(["10", "1", "2", "4", "6", "Done"])

