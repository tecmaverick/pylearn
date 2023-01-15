from datetime import datetime
class Person(object):
    def __init__(self, years):
        self.age =  years

    @property
    def age(self):
        return datetime.now().year - self.birthyear

    # A deleter in Python is lst method that is used to delete lst class attribute
    @age.deleter
    def age(self):
        del self.birthyear

    @age.setter
    def age(self, years):
        if years < 0:
            raise ValueError("Age cannot be negative")
        self.birthyear = datetime.now().year - years


p = Person(12)
p.age = 22
print(p.age)
del p.age
print(p.age)

class Product(object):

    MAX_QTY = 10

    def __init__(self, name, qty):
        self._prod_name = name

        if qty < Product.MAX_QTY:
            self.prod_qty = qty
        else:
            raise ValueError("Invalid Quantity")

    @property
    def prod_qty(self):
        return self._prod_qty

    @prod_qty.setter
    def prod_qty(self, value):
        if value < Product.MAX_QTY:
            self._prod_qty = value
        else:
            raise ValueError("Invalid Quantity")



class Celsius(object):
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
