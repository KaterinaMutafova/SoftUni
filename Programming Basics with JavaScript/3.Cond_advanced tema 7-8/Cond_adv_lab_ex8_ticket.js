function ticket(input) {
    let day = input[0];
    let price = 0
    switch (day) {
        case "Monday": 
        price = 12;
        console.log(price); break;
           
        case "Tuesday":
        price = 12;
        console.log(price); break;
       
        case "Wednesday":
        price = 14;
        console.log(price); break;
 
        case "Thursday":
        price = 14;
        console.log(price); break;

        case "Friday":
        price = 12;
        console.log(price); break;

        case "Saturday":
        price = 16;
        console.log(price); break;

        case "Sunday": 
        price = 16;
        console.log(price); break;


    }

}
ticket(["Monday"])
ticket(["Sunday"])
