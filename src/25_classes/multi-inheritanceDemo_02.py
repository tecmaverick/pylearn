class Animal:
    def __init__(self, name):
        self.__name = name

    def name(self):
        return self.__name


class Pet(Animal):
    def __init__(self, name, owner_name):
        Animal.__init__(self, name)
        self.__owner_name = owner_name

    def owner_name(self):
        return self.__owner_name


class Dog(Pet):
    def __init__(self, name, owner_name):
        Pet.__init__(self, name, owner_name)


mypet = Dog("jacky", "Abe")
print(mypet.name())
print(mypet.owner_name())
