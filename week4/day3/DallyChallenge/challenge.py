import re
chaine = input("saisissez une chaine de caractères: ")
pattern = re.compile(r"(^[a-zA-Z]+$)+")
sorti = pattern.fullmatch(chaine)

if sorti == None :
    print("Entrez uniquement des lettres")
else :
    dictionnaire = {}
    for i in range(0,len(chaine)) :
        if chaine[i] in dictionnaire :
            dictionnaire[chaine[i]].append(i)
        else :
            dictionnaire[chaine[i]] = [i]
    print(dictionnaire)


items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

liste = []
for i in items_purchase :
    if (int(items_purchase[i][1:]) < int(wallet[1:])) :
        liste.append(x)
print(liste)