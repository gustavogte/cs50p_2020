import random

class Hat:
#    def __init__(self): (no need to instance several objects)

    houses = ["Gryffindor","Hufflepuff"," Ravenclaw","Slytherin"] # this is a class variable

    @classmethod
    def sort(cls, name):
        # house = random.choice(self.houses)
        # print(name, "is in", house))
        print(name, "is in", random.choice(cls.houses))



#hat = Hat() not need to instanciate

Hat.sort("Harry")  # I am just accesing a class method, not need to instanciate
