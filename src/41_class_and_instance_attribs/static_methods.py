# static methods in python can be overridden in subclasses
# example

class shape:


    @staticmethod
    def get_name():
        return "Shape"


class square(shape):

    @staticmethod
    def get_name():
        return "Square"

# s = square()
# s.get_name() outputs "Square"

class Test:
    def method_one(self):
        print "Called method_one"
    @staticmethod
    def method_two():
        print "Called method_two"
    @staticmethod
    def method_three():
        Test.method_two()
class T2(Test):
    @staticmethod
    def method_two():
        print "T2"

#
# a_test = Test()
# a_test.method_one()
# a_test.method_two()
# a_test.method_three()
# b_test = T2()
# b_test.method_three()

# prints. Here the last outut should have been T2 instead of "Called Method two"
# Called method_one
# Called method_two
# Called method_two
# Called method_two

# to fix this, use the class method
class Test:
    def method_one(self):
        print "Called method_one"
    @staticmethod
    def method_two():
        print "Called method_two"
    @classmethod
    def method_three(cls):
        cls.method_two()

class T2(Test):
    @staticmethod
    def method_two():
        print "T2"
