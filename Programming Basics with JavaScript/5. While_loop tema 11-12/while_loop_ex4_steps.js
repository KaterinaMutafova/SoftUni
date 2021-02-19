function steps(input) {
    let target = 10000;
    let steps = 0;
    let index = 0;

    while (true) {
        steps = input[index++];
        if (steps === "Going home") {
            let stepsToHome = Number(input[index]);
            target -= stepsToHome;
            break;
        } else {
            target -= Number(steps);
        }
        if (target <=0) {
            break;
        }
        
        
    
    }
    if (target <= 0) {
        let stepsOver = Math.abs(target)
        console.log(`Goal reached! Good job!`)
        console.log(`${stepsOver} steps over the goal!`)
    } else if (target > 0) {
        let stepsLeft = Math.abs(target);
        console.log(`${stepsLeft} more steps to reach goal.`)

    }


}

steps(["1000", "1500", "2000", "6500"])
steps(["1500", "300", "2500", "3000", "Going home", "200"])
steps(["1500", "3000", "250", "1548", "2000", "Going home", "2000"])
steps(["125", "250", "4000", "30", "2678", "4682"])



