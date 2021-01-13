function password(input) {
    let passwordInDatabase = 's3cr3t!P@ssw0rd'
    if (input === passwordInDatabase) {

        console.log("Welcome")
    } else {
        console.log("Wrong password!")
    }

}
password('s3cr3t!')