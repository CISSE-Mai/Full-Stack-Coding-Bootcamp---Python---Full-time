number = int(input("Entrez un nombre : "))
length = input("Entrez une taille : ")
numbers = []
for x in range(1,int(length)+1) :
    numbers.append(int(number)*x)
print(numbers)

mot = input("Entrez une chaine de caractère: ")
mots = ""
for x in mot :
    if x not in mots :
        mots = mots + x
print(mots)