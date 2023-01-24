# ---------------------------------------------------------------------------------------------------------------------
# THe following print both strings in same like,
# as the default"end" parameter is replaced with string instead of carriageReturnLineFeed
print("same line ", end="")
print("same line ", end="")
# ---------------------------------------------------------------------------------------------------------------------

# Convert set to list
s = {1, 2, 3}
print(type(s))
l = list(s)
print(l)

# ---------------------------------------------------------------------------------------------------------------------

# Join an list containing strings
lst = ["A", "B", "C"]
print(' '.join(lst))

# ---------------------------------------------------------------------------------------------------------------------

# Join an list containing ints
lst = [1, 2, 3]
print(' '.join([str(x) for x in lst]))

# ---------------------------------------------------------------------------------------------------------------------

# Swap variables
a = 1
b = 2
a, b = b, 1
print(f"a={a} b={b}")

# ---------------------------------------------------------------------------------------------------------------------

# Enumerate list with index
lst = [1, 2, 3, 4, 5, 6, 7, 9, 10]
for i, num in enumerate(lst, start=10):
    print(i, num)

# ---------------------------------------------------------------------------------------------------------------------

# String Index
a = "ABCD"
print(a[0:3])  # This means print from 0th Index to 3rd Index of the given variable
print(a[2:3])  # This means print from 2nd Index to 3rd Index of the given variable, which is one character
print(a[-4])  # Prints 4 chars from last index position till front

# Zip two lists
a = [1, 2, 3, 4]
b = ["alpha", "beta", "gamma", "zeta"]
c = zip(a, b)
print(list(c))

# ---------------------------------------------------------------------------------------------------------------------

# Zip two lists and convert to dict
name = ['Aussie', 'American', 'European', 'Asian', 'Japanese']
age = [23, 21, 32, 11, 23]
print(dict(zip(name, age)))

# ---------------------------------------------------------------------------------------------------------------------

# Files Sorting
import os, re

sorted(glob.glob('*.png'))  # By name
sorted(glob.glob('*.png'), key=os.path.getmtime)  # By time
sorted(glob.glob('*.png'), key=os.path.getsize)  # By size

# Sort by digits contained in the filename
files = glob.glob1(img_folder, '*' + output_image_format)
# if you want sort files according to the digits included in the filename, you can do as following:
files = sorted(files, key=lambda x: float(re.findall("(\d+)", x)[0]))

# ---------------------------------------------------------------------------------------------------------------------
# Adding values in two lists using list comprehension
a = [1, 2, 3]
b = [2, 3, 4]
c = [12, 13, 14]
sum([x + y + c for x, y, c in zip(a, b, c)])

# ---------------------------------------------------------------------------------------------------------------------
# List all the loaded packages
dir()
# OUtput ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a']

# List all built-in types, keywords, functions
dir(__builtins__)
# ---------------------------------------------------------------------------------------------------------------------
# Dissasseble
from dis import dis

dis([1, 2, 3])

# ---------------------------------------------------------------------------------------------------------------------
# Adding Sets
a = {1, 2, 3, 4}
b = {11, 21, 31, 14}

# add sets
c = a | b
c = a.union(b)

# Get difference between sets
a - b
a.difference(b)

# Get common elements in both sets
a.intersection(b)

# Adding tuples to a set
mytuple = ('aa','bb')
a.add(mytuple)

# ---------------------------------------------------------------------------------------------------------------------
# Merge dicts
from collections import Counter
inventory = Counter()
loot = {"sword": 1, "bread": 3}
inventory.update(loot)

more_loot = {"sword": 1, "apple": 1}
inventory.update(more_loot)
# Here the sword gets updated to 2
# Counter({'bread': 3, 'sword': 2, 'apple': 1})

# ---------------------------------------------------------------------------------------------------------------------
# Generate all combination of two lists
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
[(x,y) for x in RANKS for y in SUITS]

# ---------------------------------------------------------------------------------------------------------------------
# When using 'is' operator the memory addresses are compared
a=None
b=None
a is b #True
id(a)
4382428816 #Memory address same for all A,B and None
id(b)
4382428816
id(None)
4382428816

a=[1,2,3]
b=[1,2,3]
a==b # True

a is b # False - because the memory address is different
id(a) # 140502013810624
id(b) # 140502013690240

# ---------------------------------------------------------------------------------------------------------------------
# Transform a method into a class method and staticmethod
# A staticmethod is a method that knows nothing about the class or instance it was called on

# A classmethod, on the other hand, is a method that gets passed the class it was called on, or the class of the instance it was called on, as first argument.
# - useful when you want the method to be a factory for the class
class C:
    @classmethod
    def f(cls, a, b):
        return a + b

    @staticmethod
    def d(a, b):
        return a + b

inst = C()
print(inst.f(1,2))
print(C.f(1,2)) # Calling like a static method