data = {'alpha':[1,2,3], 'beta':[10,20,30,40]}
print([[k,subitm] for k,v in data.items() for subitm in v])

#---------------------------------------------

grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]
for name,grade in grades:
    print(f"{name} {grade}")

for name,grade in grades:
    print(f"{name} {grade}")

# -------------------------------------------------------
# Using defaultdict as list. This will return empty list [] when accessed for non-existent keys
from collections import defaultdict
d = defaultdict(list)
print(d["nonexist_key"]) #returns []
d["nonexist_key"] = "1"

# Using defaultdict as int. This will return value of 0, when accessed for non-existent keys
d = defaultdict(int)
print(d["nonexist_key"]) #returns 0
d["nonexist_key"] = "1"

# -------------------------------------------------------
# Collections counter
from collections import Counter
data = "Hey how are you Hey where you went Hey where you were yesterday".split()
word_count = Counter(data)
print(word_count)
# The top 2 high occurance words
print(word_count.most_common(2))
