class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return print(self.name, " aboie")

    def run_speed(self):
        return print(self.age*10)

    def fight(self,other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(self.name," a gagné")
        else :
            print(other_dog.name," a gagné")