family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
somme = 0
for nom,age in family.items():
    if age< 3 :
        print("Le billet est gratuit pour: ",nom)
    elif age <= 12 :
        print("Le billet de: ",nom, " est de: 10$")
        somme = somme + 10
    else :
        print("Le billet de: ",nom, " est de: 15$")
        somme = somme + 15
print("La famille doit payer: ",somme, "$")