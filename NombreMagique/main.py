import random

NombreMagique= random.randint(1, 10)

NombreDeVies=5
print("Vous avez "+str(NombreDeVies)+" vies")
#print(NombreMagique)
while True:
    saisie = int(input("Deviner le nombre magique: "))
    if NombreMagique==saisie:
        print("Bravo vous avez trouvez le nombre magique!!!")
        break
    if NombreMagique<saisie:
        print("Le nombre mangique est plus petit que ça!!!")
    else:
      NombreDeVies=NombreDeVies-1
      print("Il vous reste: "+str(NombreDeVies)+" vies")
    if NombreMagique>saisie:
        print("Le nombre magigue est plus grand que ça!!!")
    else:
      NombreDeVies=NombreDeVies-1
      print("Il vous reste: "+str(NombreDeVies)+" vies")
    if NombreDeVies==0:
        print("Vous avez perdu!!!")
        break
