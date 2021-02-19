function graduation(input) {
    index = 0;
    let name  = input[index];
    index++;
    let grade = input[index];
    
    let sumGrades = 0;
    let counter = 0;
    let counterPoorMark = 0;

    while (true) {
        grade = Number(grade);
        index++;
        if (grade < 4) {
            counterPoorMark += 1;

            
        } else {
            sumGrades += grade;
            
        }
        if (counterPoorMark === 2) {
            break;
        }
        counter += 1;
        if (counter === 12) {
            break;
        }

        grade = input[index]
        
    }
    if (counter === 12) {
        let averageGrade = sumGrades / counter;
        console.log(`${name} graduated. Average grade: ${averageGrade.toFixed(2)}`)
    } else if (counterPoorMark === 2) {
        console.log(`${name} has been excluded at ${counter} grade`)
    }



}

graduation(["Gosho", "5", "5.5", "6", "5.43", "5.5", "6", "5.55", "5", "6", "6", "5.43", "5"])
// graduation(["Mimi",  "5", "6", "5", "6", "5", "6", "6", "2", "3"])

