garniture = input("Entrer la garniture de votre pizza : ")
garnitures = []

while garniture != "quitter":
    print("vous avez ajouté : " + garniture+ " à la pizza")
    garnitures.append(garniture)
    garniture =input("Entrer la garniture de votre pizza : ")

print(garnitures)
prix = 10+(len(garnitures)*2.5)
print(prix)


