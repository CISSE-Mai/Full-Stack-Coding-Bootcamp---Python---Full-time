import turtle

t=turtle.Turtle()
def escalier():
    for i in range(0, 5):
        t.forward(30)
        t.left(90)
        t.forward(30)
        t.right(90)
        



escalier()
turtle.done()


#une fonction qui retourne une valeur
"""def demander_age():
    age = 0
    while age == 0:
        age = input("saisir votre âge: ")
        try:
            age = int(age)
        except:
            print("ERREUR: vous devez saisir un nombre pour age")
    return age
    #print("Vous avez:  " + str(age) + "ans.")

demander_age()"""

#fonction
"""def fonction_nom():
    nom=input("saisir votre nom: ")
    print("votre nom est: "+nom)

fonction_nom()"""

#condition si
"""age=int(input("saisir votre âge: "))
condition=age>=18
print(type(condition))
if condition :
    print("Vous êtes majeur")
else:
    print("Vous ête mineur")"""


#condition si
"""age=int(input("saisir votre âge: "))
if age<2:
    print("vous êtes un bb")
elif age>2 and age<10:
    print("vous êtes un enfant")
elif age>10 and age<18:
    print("vous êtes adolescent")
elif age>18 and age<28:
    print("vous êtes majeur")
elif age>28 and age<40:
    print("vous êtes adultes")
else:
    print("vous êtes vieux")"""

#boucle for
"""nombre_max=5
for i in range(0, nombre_max):
    print(i)"""



#boucle tant que
"""m=0
while m<10:
    print("la valeur de m est: "+str(m))
    m=m+1"""



#fonction tri
"""nom= input("Votre nom: ")
age= input("Votre âge: ")

try:
    age_prochain=int(age)+1
except:
    print("ERREUR: vous devez saisir un nombre pour age")
else:
    print("Vous vous appelé " + nom + " vous avez " + age + "ans.")
print("l'an prochain vous aurez "+str(age_prochain)+"ans.")"""








