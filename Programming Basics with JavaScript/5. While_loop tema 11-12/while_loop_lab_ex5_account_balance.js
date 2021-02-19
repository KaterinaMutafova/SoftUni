function balanceAccount(input) {
    let index = 0;
    let command = input[index];
    index++;
    let totalSum = 0;
    while (command !== "NoMoreMoney") {
        let num = Number(command);
        if (num < 0) {
            console.log("Invalid operation!"); 
            break;   
        }

        totalSum += num;
        console.log(`Increase: ${num.toFixed(2)}`);

        
        command = input[index];
        index++;
        
        
            
    }

    console.log(`Total: ${totalSum.toFixed(2)}`);


}

balanceAccount(["5.51", "69.42", "100", "NoMoreMoney"]);
balanceAccount(["120", "45.55", "-150"])

