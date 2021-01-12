function aquarium(length, width, height, percent) {
    let aqLength = Number(length);
    let aqWidth = Number(width);
    let aqHeight = Number(height);
    let sandPercent = Number(percent);

    let volume = aqHeight * aqLength * aqWidth;
    let litres = volume / 1000
    let sandVolume = (sandPercent / 100) * litres;
    let aquaVolume  = litres - sandVolume;

    console.log(aquaVolume)

}
aquarium("85", "75", "47", "17")