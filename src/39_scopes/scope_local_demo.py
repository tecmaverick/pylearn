#python follows the Local -> Enclosed -> Global -> Built-in,
#LEGB scope
#Python scope heirarchy
#	Local can be inside a function or class method, for example.
#	Enclosed can be its enclosing function, e.g., if a function is wrapped inside another function.
#	Global refers to the uppermost level of the executing script itself, and
#	Built-in are special names that Python reserves for itself.

#This is also why we have to be careful if we import modules via “from a_module import *”, since it loads the variable names into the global namespace and could potentially overwrite already existing variable names

# i in global scope
i = 1


def foo():
    # i in local scope, a new variable is created when "i" is defined inside the function

    i = 5
    print(i, 'in foo()')
    print("loc in foo():", 'loc' in locals())


print(i, 'global i value before foo')

foo()

print(i, 'global i value after foo')
# here the value of global i didn't change
