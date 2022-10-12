class Dog :
    def __init__(self, name, height) :
        self.name = name
        self.height = height

    def bark(self) :
        print(self.name," goes woof!")

    def jump(self):
        print(self.name," jump ",self.height*2, " cm high!")

davids_dog = Dog("Rex",50)
print("Le chien de David: ",davids_dog.name," mesure ",davids_dog.height," cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print("Le chien de Sarah: ",sarahs_dog.name," mesure",sarahs_dog.height," cm")
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print("Le chien de Sarah est: ",sarahs_dog.name)
else:
    print("Le chien de David est: ",davids_dog.name)
