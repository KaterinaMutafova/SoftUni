function examPrep(input) {
    let counterPoorMarks = 0;
    let sumMarks = 0;
    let averageGrade = 0;
    let counter = 0
    let nameProblem = ""
    
    let index = 0;
    let numberPoorMarks = Number(input[index]);
    index++;
    let nameEx = input[index];
    index++;
    let grade = input[index];
    index++;
    

    while (nameEx != "Enough") {
        nameProblem = nameEx;
        let mark = Number(grade);
        
        if (mark <= 4) {
            counterPoorMarks += 1;
            if (counterPoorMarks === numberPoorMarks) {
                console.log(`You need a break, ${counterPoorMarks} poor grades.`)
                break;
            }

        }
        sumMarks += mark;
        counter += 1

        nameEx = input[index];
        index++;
        grade =  input[index];
        index++;

        
    }
    if (nameEx === "Enough") {
        averageGrade = sumMarks / counter
        console.log(`Average score: ${averageGrade.toFixed(2)}`)
        console.log(`Number of problems: ${counter}`)
        console.log(`Last problem: ${nameProblem}`)
    }


}

// examPrep(["3", "Money", "6", "Story", "4", "Spring Time", "5", "Bus", "6", "Enough"])
examPrep(["2", "Income", "3", "Game Info", "6", "Best Player", "4"])

