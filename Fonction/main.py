
def poser_question(question):
    global score
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print(" ", question[0])
    for i in range(len(choix)):
        print(" ", choix[i])
    print()
    reponse = input("votre reonse ")
    if reponse.lower() == bonne_reponse.lower():
        print("Bonne reponne")
        score = score+1
    else:
        print("Mauvaise reponse : ")
    print()
score=0

question1 = ("Qelle est la capitale de la France? ",("Marselle","Nice","Paris","Nantes"),"Paris")
question2 = ("Qelle est la capitale de ll'Italie? ",("Rome","Venise","Pise","Florence"),"Rome")

"""poser_question("Qelle est la capitale de la France? ","Marselle","Nice","Paris","Nantes","c")
poser_question("Qelle est la capitale de l'Italie? ","Rome","Venise","Pise","Florence","a")"""


poser_question(question1)
poser_question(question2)

print(score)





"""nom_chauffeur_km=["patrick","paul","Marc","jean","pierre","Martin","Maxim"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

noms_et_distances=[("patrick",1.5), ("paul",2.2), ("Marc",0.4)]

nom_et_distance_min=noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print("Distance minimale",nom_et_distance_min[1], "nom du chauffeur", nom_et_distance[0])"""


"""nom_chauffeur_km=["patrick","paul","Marc","jean","pierre","Martin","Maxim"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
index_min = 0
distance_min = distance_chauffeur_km[0]
for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i

print("La distance minimale est : ", distance_min, "km")
print("L'index est: ", index_min)
print("et le nom du chauffeur est : ", nom_chauffeur_km[index_min])"""



"""conteneur = []
nom = " "
while nom!="":
    nom = input("saisir votre nom: ")
    conteneur.append(nom)

print(conteneur)
conteneur.sort()
for nom in conteneur:
    print(nom)"""




"""def afficher_infos_personne(id_p):
    nom= input("saisir votre nom: "+str(id_p)+ " : ")
    age= input("saisir votre age: "+str(id_p)+ " : ")
    print("La personne"+str(id_p)+" est "+nom+ ", son âge est: "+str(age)+ " ans")
    print("Le nom possède "+str(len(nom))+" caractères")

nombre_personne = int(input("saisir le nombre de personne: "))
for i in range(1, nombre_personne):
    afficher_infos_personne(i)"""




"""def _estmajeur():
    age=int(input("saisir votre âge: "))
    if age>18:
        print("Vous êtes majeur")
    else:
        print("mineur!!!!!")


_estmajeur()"""



"""def afficher_les_infos_personne(nom="", age=0):

    if nom=="":
        print("Le nom n'a pas été renseigné")
        return


    if age==0:
        print(f"La personne est: {nom}")
    else:
        print("votre nom est: ", nom, " et vous avez ", age, "ans")



    print("le nom contient ", len(nom), " caractère")




afficher_les_infos_personne()



nom=input("saisir votre nom: ")
age=int(input("saisir votre âge: "))"""