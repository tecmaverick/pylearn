# class attrib demo

# when to use class attribs
# 1. Storing Constants
# 2. Defining default vals
# 3.
class car:
    # defining class attribute car_counter, which is equalivent of defining a static variable
    # all instances of the class have access to car_counter, and can be accessed as a property of the class itself
    # ex:
    # c1 = car("benz","2012")
    # c2 = car("audi","2011")
    # c3 = car("bmw","2013")
    # print car.car_counter value as 3
    # print c1.car_counter value as 3

    car_counter = 0

    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.serial = car.car_counter

        # increment class attrib counter when earch car is initialized
        car.car_counter += 1

        # trying to do this via like this, will cause the instance attribute and NOT class attribute
        # to be modified and not class attribute
        # self.car_counter += 1

    # defining a static methond in a class. NOTE: these is not self argument
    # the function can be called classname.<staticmethodname>() eg. car.get_car_counter()
    # or classinstance.<static_method_name>() eg c2.get_car_counter()
    @staticmethod
    def get_car_counter():
        return car.car_counter

    # The instance namespace takes supremacy over the class namespace:
    # if there is an attribute with the same name in both,
    # the instance namespace will be checked first and its value returned

    # Note: to view class instance vars use
    # classname.__dict__

    # to view instance class vars use
    # class_instance_name.__dict__

    # Note: if a class instance is set the same name as class variable, then the variable
    # value will only be different for that specific instance. Ex:
    # c1 = car("benz","2012")
    # c2 = car("audi","2011")
    # c3 = car("bmw","2013")
    # c3.car_count = 1000

    # print car.car_count will print 3
    # print c3.car_count will print 1000, because only for this class instance contains the same var as class var
    # print car.car_count will print 3
    # print c1.car_count will print 3

