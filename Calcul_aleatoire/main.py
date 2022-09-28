import random



score=0
Calcul = input("choisir l'opération: ")

if Calcul=="soustraction":
    for i in range(1,4):
        Nombre_a = random.randint(1, 10)
        Nombre_b = random.randint(1, 10)
        print("Question N°"+str(i))
        print(Nombre_a, "-", Nombre_b)
        resultat = int(input("Entrer le resultat: "))
        operation = Nombre_a - Nombre_b
        if resultat != operation:
            print("Mauvaise reponse")
        else:
            print("Bravo, bonne reponse")
            score=score+1



elif Calcul=="addition":
    for i in range(1,4):
        Nombre_a = random.randint(1, 10)
        Nombre_b = random.randint(1, 10)
        print("Question N°"+str(i))
        print(Nombre_a, "+", Nombre_b)
        resultat = int(input("Entrer le resultat: "))
        operation = Nombre_a + Nombre_b
        if resultat != operation:
            print("Mauvaise reponse")
        else:
            print("Bravo, bonne reponse")
            score=score+1



elif Calcul=="division":
    for i in range(1,4):
        Nombre_a = random.randint(1, 10)
        Nombre_b = random.randint(1, 10)
        print("Question N°"+str(i))
        print(Nombre_a, " : ", Nombre_b)
        resultat = int(input("Entrer le resultat: "))
        operation = Nombre_a // Nombre_b
        if resultat != operation:
            print("Mauvaise reponse")
        else:
            print("Bravo, bonne reponse")
            score=score+1



elif Calcul=="multiplication":
    for i in range(1,4):
        Nombre_a = random.randint(1, 10)
        Nombre_b = random.randint(1, 10)
        print("Question N°"+str(i))
        print(Nombre_a, "*", Nombre_b)
        resultat = int(input("Entrer le resultat: "))
        operation = Nombre_a * Nombre_b
        if resultat != operation:
            print("Mauvaise reponse")
        else:
            print("Bravo, bonne reponse")
            score=score+1




print("Vous avez : "+str(score)+" points")
