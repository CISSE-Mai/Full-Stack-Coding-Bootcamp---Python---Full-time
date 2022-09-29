fruits_preferes = input("saisir vos fruits préférés : ")
print(fruits_preferes)
liste = fruits_preferes.split(" ")
print(liste)
fruits_verif = input("saisir vos fruits préférés : ")
if fruits_verif in liste :
    print("vous avez choisit un de vos fruit pref")
else:
    print("vous avez saisi un nouveau fruit")