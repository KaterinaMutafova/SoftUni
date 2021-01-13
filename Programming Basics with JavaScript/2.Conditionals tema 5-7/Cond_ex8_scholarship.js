function scholarship(input) {
    let income = Number(input[0]);
    let averageGrades = Number(input[1]);
    let minSalary = Number(input[2]);

    let excellentScholarship = Math.floor(25 * averageGrades);
    let socialScholarship = Math.floor(0.35 * minSalary);

    if (averageGrades >= 5.50 && income < minSalary) {
        if (excellentScholarship > socialScholarship) {
            console.log(`You get a scholarship for excellent results ${excellentScholarship} BGN`);
        } else if (excellentScholarship < socialScholarship) {
            console.log(`You get a Social scholarship ${socialScholarship} BGN`)
        } 
    } else if (averageGrades >= 5.50) {
        console.log(`You get a scholarship for excellent results ${excellentScholarship} BGN`);
    } else if (averageGrades > 4.50 && averageGrades < 5.50 && income < minSalary) {
        console.log(`You get a Social scholarship ${socialScholarship} BGN`);
    } else {
        console.log("You cannot get a scholarship!"); 
    } 
    
}

scholarship(["480.00", "4.60", "450.00"])
scholarship(["300.00", "5.65", "420.00"])