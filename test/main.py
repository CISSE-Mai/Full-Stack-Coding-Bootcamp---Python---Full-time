
"""def a(n, limit):
    if n > limit:
        return
    print("n: ", n)
    a(n*n, limit)



a(2, 1)"""


"""def demander_choix_utilisateur(min, max):
    reponse_str = input("quel est votre choix entre " + str(min) + " et " + str(max) + " : ")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print("ERREUR : Vous devez saisir un nombre entre ", min, " et ", max)
        return reponse_int
    except:
        print("ERREUR: Vous devez rentrer un nombre")

choix = demander_choix_utilisateur(1, 4)
print("choix de l'utilisateur: ", choix)"""


"""def a():
    print("Debut de la fonction")
    for i in range(0, 100):
        if i>20:
            return
        print(i)
    print("Fin de la fonction")

a()"""



"""def somme(titre, **nombre):
    print("TITRE: ", titre)
    resultat=0
    for i in nombre.values():
        resultat +=i
    return resultat

print(somme("la somme des notes", ig=5, rt=6))"""


a= 10
print(a>10)
