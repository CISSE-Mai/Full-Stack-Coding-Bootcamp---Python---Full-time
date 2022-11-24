def Temps_de_Chargement(site):
    import requests
    import time

    debut = time.time()
    requests.get(site)
    temps= time.time() - debut
    return temps

def affiche(site,temps):
    print(f"Le temps de Chargement de {site} est ==> {temps}")

affiche("https://www.google.com/",Temps_de_Chargement("https://www.google.com/"))
affiche("https://www.imdb.com/",Temps_de_Chargement("https://www.imdb.com/"))