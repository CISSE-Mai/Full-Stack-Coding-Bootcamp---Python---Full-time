#Appel de la bibliothèque
#**************programme avec gestion événement*****************
#Appel de la bibliothèque
from tkinter import *
#---------définition de la fonction de calcul de TVA------------
def calculTVA():
    global ht, ttc
    #conversion en float du montant HT
    pht=float(ht.get())
    #calcul de la TVA avec un taux de 20%
    ttc=round(pht*(1+(20/100)),2)
    #actualisation du libellé de la fenêtre affichant le ttc
    ttcLabel.configure(text="Le montant TTC est "+str(ttc))

#-------------création de l'interface graphique-----------------
#Création de la fenêtre et de son titre
window=Tk()
window.title("Calcul de TVA")
#Mise en place d'un widget de label
htLabel = Label(window, text="Saisir le montant Hors Taxe")
htLabel.pack()
#Mise en place d'un widget de saisie
ht = StringVar()
ht.set("12 ?")
saisieHT = Entry(window, textvariable=ht, width=10)
saisieHT.pack()
#Mise en place d'un widget de bouton
bouton1 = Button(window, text="CALCULER", width=8, command=calculTVA)
bouton1.pack()
#Mise en place d'un widget de label pour afficher le TTC
ttcLabel = Label(window, text="Le montant TTC est")
ttcLabel.pack()
#-------------gestion des événements----------------------------
#Lancement de la boucle des événements de la fenêtre
window.mainloop()