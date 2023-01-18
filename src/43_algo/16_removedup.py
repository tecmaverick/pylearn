import random

words = "This is a test message from a list of test messages".split(" ")
dict = {}

# Time complexity is O(N)
for _ in range(1000):
    word = random.choice(words)
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

print([(k,v) for k,v in dict.items()])
