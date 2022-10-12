class Farm:
    def __init__(self, name):
        self.name = name
        self.animal = {}

    def add_animal(self, name, nombre=1):
        if name in self.animal :
            self.animal.update({name : self.animal[name]+nombre})
        else :
            self.animal.update({name : nombre})

    def get_info(self) :
        mot = ""
        print(f"{self.name}'s farm\n")
        for x in self.animal :
            mot += x + " : " + str(self.animal[x]) + "\n"
        return mot

    def get_animal_types(self) :
        animal = []
        for x in self.animal :
            animal.append(x)
        return sorted(animal)


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())