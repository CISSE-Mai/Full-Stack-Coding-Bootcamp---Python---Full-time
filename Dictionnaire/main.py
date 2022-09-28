
"""Etudiant = {'nom': "CISSE", 'ecole':"IAM", 'classe': "IG3", 'age': 15}
Etudiant["prenom"] = "Maimounata"
rajout_tuple = (805663, 65843804, "cmail@gmail.com")
Etudiant['rajout_tuple'] = rajout_tuple


print(Etudiant)"""

"""personnes = [

    ("Melanie", 25, 1.6)
    ("paul", 25, 1.6)
    ("jacques", 25, 1.6)
    ("Martin", 25, 1.6)
]
def obtenir_infos(nom, liste):
    for i in range personnes:
         
"""

"""personnes_dict = {
    "Melanie": (25,1.6),
    "paul": (29 , 1.8),
    "jacques": (35,1.75),
    "Martin": (16,1.65)
}
infos = personnes_dict.get("claire")
if not infos:
    print("La clef n'existe pas")
else:
    print(infos)"""


noms = ["jean", "Sophie", "Martin","christophe", "zoe"]

#noms_supplementaires = ["christophe", "zoe"]

#noms.append(noms_supplementaires)

#for e in (noms_supplementaires):
    #noms.append(e)
   # noms.extend(noms_supplementaires)
    #noms += noms_supplementaires
#noms.sort(key=lambda nom: len(nom), reverse=True)

"""t=noms[0]
noms[0]=noms[4]
noms[4]=t"""
#noms[0], noms[4] = noms[4], noms[0]

"""noms_joinn = "_".join(noms)

print(noms_joinn)

a = "jean,Sophie,Martin,christophe, zoe"
noms_split = " ".split(noms)
print(noms_split)"""

element_cherche = "Martin"
nb_occurences = noms.count(element_cherche)
print("nb_occurences", nb_occurences)



