class Demo:
    def some_method(self, name):
        return name

v = Demo()
print(v.__class__.__name__)

# All internal and external methods
print(dir(v))

# Get the class type
print(type(v))
# Get the class type
print(isinstance(v, Demo))