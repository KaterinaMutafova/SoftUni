function names(input) {
    let index = 0
    let name = ""
   
     while (name != "Stop") {
         name = input[index]
         if (name === "Stop") {
             break;
         } else {
            console.log(name)
         }
         index++

     }






}

names(["Nakov", "SoftUni", "Sofia", "Bulgaria", "SomeText", "Stop", "AfterStop", "Europe", "HelloWorld"])
