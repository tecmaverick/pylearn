#Python uses loose typing, i.e. the base class
#can have methods which is defined in child class

class Shape:
	def name(self):
		return self._name

class Circle(Shape):
	def __init__(self, radius, name):
		self._radius = radius
		self._name = name

class Square(Shape):
	def __init__(self, measure, name):
		self._measure = measure
		self._name = name


c1 = Circle(12,"c1")
sq1 = Square(5,"sq1")

print c1.name()
print sq1.name()

#ths will throw an exception as name is not defined in the base class
shp = Shape()
print shp.name()
