import itertools

# for in loop, start at 5 and increment by 5
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end =" ")

#Cycle between values
count = 0

for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end = " ")
        count += 1