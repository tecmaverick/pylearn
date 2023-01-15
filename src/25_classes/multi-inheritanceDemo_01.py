class Animal:
    def __init__(self, name):
        self.__name = name

    def name(self):
        return self.__name


class Pet:
    def __init__(self, owner_name):
        self.__owner_name = owner_name

    def owner_name(self):
        return self.__owner_name


class Dog(Animal, Pet):
    def __init__(self, name, owner_name):
        Animal.__init__(self, name)
        Pet.__init__(self, owner_name)


mypet = Dog("jacky", "Abe")
print(mypet.name())
print(mypet.owner_name())
