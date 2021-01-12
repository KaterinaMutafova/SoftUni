function archCalculator(name, quantity){
    let projectDuration = 3
    let nameArch = name
    let projectNumber = Number(quantity)

    let hoursWorking = projectDuration * projectNumber
    
    console.log(`The architect ${nameArch} will need ${hoursWorking} hours to complete ${projectNumber} project/s.`)

}
archCalculator("George", "4")