

def Nom(s):
    if len(s)<=4:
        print("Bonjour "+s)
        return True
    else:
        return False

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]


Nom_4lettres = filter(Nom,people)

print(list(Nom_4lettres))