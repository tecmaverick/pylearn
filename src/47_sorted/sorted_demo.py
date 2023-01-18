data = [
    {"name": "animal2", "type": "wild", "weight": 50, "height": 20},
    {"name": "animal1", "type": "domestic", "weight": 20, "height": 30},
    {"name": "animal3", "type": "wild", "weight": 55, "height": 25},
    {"name": "animal4", "type": "wild", "weight": 25, "height": 15}
]
# Sort dict by multiple fields
data = sorted(data, key=lambda x: (x["type"], x["height"]))
for row in data:
    print(row)


# ******************************************************************************
#  Sort class - Implement "lt" to handle sort
class myemp:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def __lt__(self, other):
        return self._age < other._age and \
               self._salary < other._salary

    def __repr__(self):
        return f"{self._name},{self._age},{self._salary}"


lst_emps = [
    myemp("ajp0", 30, 1300),
    myemp("ajp1", 10, 900),
    myemp("ajp4", 40, 1400),
    myemp("ajp2", 50, 1500),
    myemp("ajp3", 20, 200)
]
print(sorted(lst_emps))

# ******************************************************************************

#  Sort class instance without "lt". Using class attribute
import operator


class myemp:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def __repr__(self):
        return f"{self._name},{self._age},{self._salary}"


lst_emps = [
    myemp("ajp0", 30, 1300),
    myemp("ajp1", 10, 900),
    myemp("ajp4", 40, 1400),
    myemp("ajp2", 50, 1500),
    myemp("ajp3", 20, 200)
]
# Solution 1
print(sorted(lst_emps, key=operator.attrgetter('_age', '_salary')))

# Solution 2
print(sorted(lst_emps, key=lambda x: (x._age, x._salary)))
# ******************************************************************************

# Sort multiple lists, based on the first list item which is city
sales_city = ['Sanfransisco', 'Los Angles', 'New York', 'Atlanta']
sales_comm = [20000, 30000, 34000, 14000]
sales_products = ['Perfume', 'Shaver', 'Laptop', 'Backpack']

zipped = list(zip(sales_city, sales_comm, sales_products))
zipped.sort()
for row in zipped:
    print("{} {} {}".format(*row))

d1, d2, d3 = zip(*zipped)
print(d1)
print(d2)
print(d3)

# ******************************************************************************
# Sort multiple lists, based on the 3rd & 4th column in the list
data = [
    [1, "Alpha", "North", 2],
    [4, "Alpha1", "North", 1],
    [2, "Beta", "West", 0],
    [3, "Cierra", "South", 1]
]
# Sort by last two fields
# Option 1
data.sort(key=operator.itemgetter(2, 3))

# Option 2
data.sort(key=lambda x: (x[2], x[3]))

for row in data:
    print(*row)

# ******************************************************************************
# Using custom function to sort
import functools
people = ["Student1 B", "Student2 C", "Student3 A", "Student4 A"]


def compare(studenta, studentb):
    # Get the student grande like A,B,C then its ASCII value and compare
    studenta_score = ord(studenta.split(" ")[1])
    studentb_score = ord(studentb.split(" ")[1])

    if studenta_score < studentb_score:
        return -1
    elif studenta_score > studentb_score:
        return 1
    else:
        return 0


# Calling custom compare. In Python3 this requires 'cmp_to_key'.
# In Py2 calling sort with custom function is people.sort(key=compare)
people.sort(key=functools.cmp_to_key(compare))
print(people)
