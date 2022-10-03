let myWatchedSeries =["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesSentence = myWatchedSeries.toString();
console.log(myWatchedSeriesSentence);

console.log("I watched" + myWatchedSeriesLength + "series :"+ " "+myWatchedSeriesSentence);
myWatchedSeries[2]="friends";
myWatchedSeries.push("Fabiola");
myWatchedSeries.unshift("Bobodioufs");
myWatchedSeries.shift()
console.log("la troisieme lettre de la serie "+myWatchedSeries[2]);
console.log(myWatchedSeries);
