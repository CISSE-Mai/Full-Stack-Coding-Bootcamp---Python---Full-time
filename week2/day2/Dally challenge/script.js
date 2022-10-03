let sentence = "Le film is not pas  bad si mal, j'aime bien";
let wordNot = "not";
let wordBad = "bad";
        for(let i=0; i<sentence.length; i++ ){
            var Ind1 = sentence.indexOf('not');
            var Ind2 = sentence.indexOf('bad');
            if(Ind1<Ind2){
                for(i=Ind1; i=Ind2; i++){
                    sentence =sentence.replace("i", " ");
                }
                console.log(sentence + "good")

            }else{console.log(sentence)};
        }