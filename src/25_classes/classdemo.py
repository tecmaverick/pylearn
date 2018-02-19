# """ model for person """

# In python everythings Public by default

# empty class
class Person:
    pass


""" model for book """

#Python class naming convention is CamelCase
class Book:
    # __init__ in python is NOT a ctor as in Java, C#.
    # it simply initializes the class which is already created
    def __init__(self, isbn):
        # this auto creates the instance variable "_number"
        # the underscore notation is to signal this is a internal\private variable
        # though this doesn't prevent from being accessed
        self._isbn_number = isbn

    # self represent the classes current instance
    # the 'self' keyword is analogous to 'this' keyword in java or csharp
    def isbn(self):
        return self._isbn_number


# Instantiating book
book = Book(isbn="12ABB-23P23")
print book.isbn()

#The call to the ISBN method is a syntatic sugar of the following
print Book.isbn(book)

#in python polymorphism is achieved through objects having
#the same method or proerties, rather validating over 
#base class, inteface etc
#Python uses DuckTypeing, which is object is evaluated at the time of use
