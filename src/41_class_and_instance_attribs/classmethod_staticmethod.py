# @staticmethod decorator
# use when
# 1. No access is needed to class instance objects
# 2. For Deterministic functions. Deterministic functions always return the same result any time
#    they are called with a specific set of input values. Ex. AddDate(), GetDate(), Avg(),
#    Nondeterministic functions returns different results each time they are called
#    with a specific set of input values

# @classmethod decorator
# use when
# 1. Requires access to the class object to call other class methods or the ctor.
# ex:
import math
class MyMath:
    cls_instance_counter = 0

    def __init__(self, obj_owner=None):
        self.obj_owner = obj_owner
        MyMath.cls_instance_counter +=1

    @staticmethod
    def pi_val():
        return math.pi

    @staticmethod
    def add(fno, sno):
        return fno + sno

    # here the cls refers to the same class MyMath
    # unlike instance methods, classmethod doesn't require self param
    @classmethod
    def get_class_count(cls):
        return cls.cls_instance_counter

    # this method creates a class of MyMath with the text as parameter
    @classmethod
    def create_class(cls):
        return cls("ClassFactory Provisioned")


# a = MyMath()
# b = MyMath()
# c = MyMath()
# calling class method via class name MyMath.get_class_count() prints 3
# calling class method via instance a.get_class_count() prints 3
# calling static method via instance a.pi_val() prints value of PI
# calling static method via class name MyMath.pi_val() prints value of PI


# Note: Class methods and static methods can be called on either instance or on class name itself
