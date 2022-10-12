class Zoo :
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        list(map(lambda x : print(x),self.animals))

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        ani = sorted(self.animals)
        animal ={}
        animal.update({1:ani[0]})
        j=2
        for i in range(1,len(ani)) :
            if ani[i][0] == ani[i-1][0] :
                animal.update({j-1: animal[j-1]+[ani[i]]})
            else :
                animal.update({j: [ani[i]]})
                j+=1
        return animal

    def get_groups(self,animal,animaux):
        print(f"{animal}/")
        for x in animaux :
            if animal[0] == animaux[x][0][0] :
                print(f"{animaux[x]}")


ramat_gan_safari = Zoo("sss")

while True :
    ani = input("Ajoute un animal au zoo: ")
    if ani.lower() != "exit" :
        ramat_gan_safari.add_animal(ani)
    else:
        break
    print("Entrez 'exit' pour quitter")

ramat_gan_safari.get_animals()
print("\n")

while True :
    ani = input("supprime un animal: ")
    if ani.lower() != "exit" :
        ramat_gan_safari.sell_animal(ani)
    else :
        break
    print("Entrez 'exit' pour quitter")

ramat_gan_safari.get_animals()
print("\n")

animals = ramat_gan_safari.sort_animals()
print(animals)
print('\n')

animal = input("Entrez le nom d'un animal existant : ")
ramat_gan_safari.get_groups(animal,animals)