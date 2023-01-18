import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inbuilt shuffle
random.shuffle(a)
print(a)

# ************************************************

import datetime
def shuffle(data,seed=None):
    seed_val = datetime.time.microsecond if seed is None else seed
    random.seed(seed_val)

    for i in range(len(data)):
        swapIdx = random.randint(0,len(data)-1)
        data[i],data[swapIdx] = data[swapIdx],data[i]

    return data

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffle(a))