function area(arg1, arg2, arg3){
    if (arg1 === "square") {
        let side = Number(arg2);
        let area = side * side;
        console.log(area.toFixed(3))
    } else if (arg1 === "rectangle") {
        let side1 = Number(arg2);
        let side2 = Number(arg3);
        let area = side1 * side2;
        console.log(area.toFixed(3));
    } else if (arg1 === "circle") {
        let radius = Number(arg2);
        let area = Math.PI * radius * radius;
        console.log(area.toFixed(3));
    } else if (arg1 === "triangle") {
        let side = Number(arg2);
        let height = Number(arg3);
        let area = (side * height) /2
        console.log(area.toFixed(3));
    }

}
area("square", "5")
area("rectangle", "7", "2.5")
area("circle", "6")
area("triangle", "4.5", "20")