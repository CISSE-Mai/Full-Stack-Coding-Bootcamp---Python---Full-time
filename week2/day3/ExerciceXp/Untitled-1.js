//Exercicie 1

let people = ["Greg", "Mary", "Devon", "James"];
people[0].pop()
let last = people.at(-1);


// Exercice 3

let numberForUser = Number(prompt("Give one number : "));
while(numberForUser <10 ){
    let numberForUser = Number(prompt("Give one number : "));
     alert(typeof(numberForUser));
}



//Exercice 4


let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor +" et "+ building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1]);


//Exercicie 7

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let nom = [];
for (let i of names){
  let code = names[i][0];
  nom.push[code];
}

console.log(sort(nom));