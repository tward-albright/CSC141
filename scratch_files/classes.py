class Pet:
    def __init__(self, type, name, age, stinky=False):
        self.type = type
        self.name = name
        self.age = age
        self.stinky = stinky


class NotPet:
    def __init__(self, name, age, *pets):
        self.name = name
        self.pets = pets
        self.age = age


jordan = Pet("border collie", "Jordan", 2, stinky=True)
jacky = Pet("labrador", "Jacky", 3, stinky=True)
paige = Pet("fox", "Paige", 45)
rae = NotPet("Rae", 18, jacky)
