import itertools

staff = ["Ann","Abe","Tiran","Spea","Geo","Moi","Andy"]
staff = ["Ann","Abe","Tiran"]

# Order matters, hence the element will be shuffled throughout the result. This leads to bigger resultset
print(list(itertools.permutations(staff,3)))

# Order DOESNT matter, hence the element will NOT be shuffled throughout the result. This leads to smaller resultset
print(list(itertools.combinations(staff,3)))

