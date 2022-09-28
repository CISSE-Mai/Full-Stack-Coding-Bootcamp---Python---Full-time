import random



score=0
choix = input("choisir entre la multiplication, l'addition, la soustraction et la division: ")

if choix=="multiplication":
    for i in range(1,5):
        Nombre1 = random.randint(1, 10)
        Nombre2 = random.randint(1, 10)
        print("Question N°", i ,"sur 4")
        print(Nombre1, "*", Nombre2)
        resultat = int(input("Entrer le resultat: "))
        if resultat != Nombre1 * Nombre2:
            print("Reponse incorrect")
        else:
            print("Reponse correct")
            score=score+1


elif choix=="addition":
    for i in range(1,5):
        Nombre1 = random.randint(1, 10)
        Nombre2 = random.randint(1, 10)
        print("Question N°", i ,"sur 4")
        print(Nombre1, "+", Nombre2)
        resultat = int(input("Entrer le resultat: "))
        if resultat != Nombre1 + Nombre2:
            print("Reponse incorrect")
        else:
            print("Reponse correct")
            score=score+1


elif choix=="soustraction":
    for i in range(1,5):
        Nombre1 = random.randint(1, 10)
        Nombre2 = random.randint(1, 10)
        print("Question N°", i ,"sur 4")
        print(Nombre1, "-", Nombre2)
        resultat = int(input("Entrer le resultat: "))
        if resultat != Nombre1 - Nombre2:
            print("Reponse incorrect")
        else:
            print("Reponse correct")
            score=score+1


elif choix=="division":
    for i in range(1,5):
        Nombre1 = random.randint(1, 10)
        Nombre2 = random.randint(1, 10)
        print("Question N°", i ,"sur 4")
        print(Nombre1, " : ", Nombre2)
        resultat = int(input("Entrer le resultat: "))
        if resultat != Nombre1 // Nombre2:
            print("Reponse incorrect")
        else:
            print("Reponse correct")
            score=score+1



print("Le score est de : ",score,"/4")
