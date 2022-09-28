import random

nombre_magigue = random.randint(0, 10)

nombre_de_vies = 4
print("Vous avez "+str(nombre_de_vies)+" chances")

try:
    while nombre_de_vies > 0 :
        nombre_saisi = int(input("Quel est le nombre magique? "))
        if nombre_saisi < nombre_magigue :
            nombre_de_vies -=1
            print("Le nombre magique est plus grand")
            print("Il vous reste "+str(nombre_de_vies)+" chances")
        elif nombre_saisi > nombre_magigue :
            nombre_de_vies -= 1
            print("Le nombre magique est plus petit")
            print("Il vous reste "+str(nombre_de_vies)+" chances")
        else:
            print("Bravo vous avez pu deviner le nombre magique")
            break
        if nombre_de_vies == 0 :
            print("Vous avez perdu!!!!!!")
except :
    print("Veuillez saisir uniquement des nombre")