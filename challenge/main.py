import random

chaine=input("saisir une chaine: ")
if len(chaine)<10:
    print("chaine courte")
elif len(chaine)>10:
    print("chaine longue")
else:
    print("bravo")
print("...")


chaine2=""
for element in chaine:
    chaine2=chaine2+element
    print(chaine2)

print("...Bonus...")

list = list(chaine)
print(list)
random.shuffle(list)
chaine="".join(list)
print(list)