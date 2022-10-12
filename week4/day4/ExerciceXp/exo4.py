import random
def aleatoire(number) :
    nombre = random.randint(1,100)
    if nombre == int(number) :
        print("Bravooo!!!")
    else :
        print("Réessayez")
    print("Vous avez saisi: ",number)
    print("Le nombre magique est: ",nombre)
aleatoire(12)