function chekNumber(nombre) {
    Type = Number(nombre);
    if (!Type) {
        console.log("not a number ");
        return false;
    }else {
        return true;
    }
}

function inputNumber() {
    let nombre;
    do {
        nombre = prompt("Entrez un nombre de bouteille pour commencer","99");
    } while (!chekNumber(nombre))
    return nombre;
}


function sing() {
    let nombre=inputNumber();
    console.log("We start the song at",nombre,"bottles")
    nombre= nombre-1;
    console.log("-> Take _1_ down, pass it around");
    console.log("-> we have now" , nombre , "bottles");
    for ( let i = 2; i < nombre; i++) {
        console.log("-> Take _" + i + "_ down, pass them around");
        console.log("-> we have now" , nombre-i , "bottles");
        nombre = nombre-i;
    }
    console.log("-> Take _" + nombre + "_ down, pass them around");
    console.log("-> we have now 0 bottle");
}

sing();