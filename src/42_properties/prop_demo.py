


class Product:

    MAX_QTY = 10

    def __init__(self, name, qty):
        self._prod_name = name

        if qty < Product.MAX_QTY:
            self._prod_qty = qty
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



class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

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
