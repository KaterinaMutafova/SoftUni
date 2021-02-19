function factoriel(input) {
    let number = Number(input[0]);
    let factoriel = 1;

    for (let i = 2; i <= number; i++){
        factoriel *= i;
        
    }
    console.log(factoriel);

}
factoriel(["8"])