class Car:
    def drive(self):
        print("Driving car")


class AllWheelDrive:
    def drive(self):
        print("All wheel drive engaged")


class LandCruiser(Car, AllWheelDrive):
    pass


mycar = LandCruiser()

# Here the MRO (Method Resolution Order) specifies that methods should be inherited from the leftmost superclass first
#  which is Car
mycar.drive()
