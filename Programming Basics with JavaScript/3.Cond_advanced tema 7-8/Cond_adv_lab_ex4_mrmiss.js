function mrMiss(input) {
    let age = Number(input[0]);
    let sex = input[1];
    if (sex == "m") {
        if (age < 16) {
            console.log("Master");
        } else if (age >= 16) {
            console.log("Mr.");
        }
    } else if (sex == "f") {
        if (age < 16) {
            console.log("Miss");
        } else if (age >= 16) {
            console.log("Ms.");
        }
    }
  
}

mrMiss(["12", "f"])
mrMiss(["25", "f"])
mrMiss(["17", "m"])
mrMiss(["13.5", "m"])