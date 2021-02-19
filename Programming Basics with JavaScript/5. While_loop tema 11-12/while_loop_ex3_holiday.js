function holiday(input) {
   

    let budgetForTrip = Number(input[0]);
    let moneyBeginning = Number(input[1]); 

    let index = 2;

    // let action = input[index];
    // let currentMoney = input[index];

    let counterDays = 0
    let counterSpend = 0
  

    while (true) {
        let operation = input[index++];
        let amount = Number(input[index]);
        

        if (operation === "spend") {
            counterSpend++;
            counterDays += 1
            if (moneyBeginning < amount) {
                moneyBeginning = 0;
            } else if (moneyBeginning > amount) {
                moneyBeginning -= amount
            }
            

        } else if (operation === "save") {
            counterSpend = 0;
            counterDays += 1
            moneyBeginning += amount
        }
        
        if (counterSpend === 5) {
            console.log("You can't save the money.")
            console.log(counterDays)
            break;
        }
        if (moneyBeginning >= budgetForTrip) {
            console.log(`You saved the money for ${counterDays} days.`)
            break;
        }

        index++;
            
        
    }
    
    



}

holiday(["2000", "1000", "spend", "1200", "save", "2000"])
holiday(["110", "60", "spend", "10", "spend", "10", "spend", "10", "spend", "10", "spend", "10"])
holiday(["250", "150", "spend", "50", "spend", "50", "save", "100", "save", "100"])


