'''famille = int(input("entrer l'age de cette personne:"))
bibi = "le billet est gratuit"
baba = "le billet est de 10 $"
bebe = "le billet est de 15$"
if famille < 3:

    print(bibi)

elif famille >= 3 and famille <= 12:

    print(baba)


elif famille > 12:

    print(bebe)
else:
    print("rien")

users = " quel est l'age de cette personne qui veut un billet ?"
print(users)
age = "l'age  de cette personne de la famille entrer est de", famille, "ans"
print(age)
bilet_total = "la liste de billet sont:", bibi, baba, bebe
print(bilet_total)

nom = input("entre votre nom:")
prenom = input('entrer votre prenom:')
age = input("entrer votre age:")
list = [nom, prenom, age]
print(list)
famille = int(input("entrer l'age de cette personne:"))
bibi = "le billet est gratuit"
baba = "le billet est de 10 $"
bebe = "le billet est de 15$"
if famille < 3:

    print(bibi)
elif famille >= 3 and famille <= 12:

    print(baba)
elif famille > 12:

    print(bebe)
else:
    print("rien")

users = " quel est l'age de cette personne qui veut un billet ?"
print(users)
age = "l'age  de cette personne de la famille entrer est de", famille, "ans"
print(age)
bilet_total = "la liste de billet sont:", bibi, baba, bebe
print(bilet_total)

nom = input("entre votre nom:")
prenom = input('entrer votre prenom:')
age = int(input("entrer votre age:"))
list = [nom, prenom, age]
print(list)
if age >=16 and age<=21 :
    print(list)
else:
    list.remove(list)
print(list)'''





nbre = int(input("saisir le nbre de personnes : "))
somme = 0
nbreb = 0
while nbre<=0 :
    nbre = int(input("saisir le nbre de personnes : "))

for i in range(nbre) :
    age = int(input("saisir l'âge de la personne : "))
    while age<=0 and age>=135 :
        age = int(input("saisir l'âge de la personne : "))
    if age>3 and age <=12 :
        somme = somme + 10
        nbreb = nbreb + 1
    elif age > 12 :
        somme = somme + 15
        nbreb = nbreb + 1
print("la somme total est : ",str(somme))
print("le nombre de billet est : ",str(nbreb))

ado = ["Maï", "CISSE"]
print(ado)
for i in ado :
    a = int(input("sasir votre âge : "))

    if a>=16 and a<=21 :
        print("vous pouvez suivre le film")
    else:
        ado.remove(i)
print(ado)