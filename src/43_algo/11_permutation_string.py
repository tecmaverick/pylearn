# The number of elements for permutations for a given string is N Factorial = N! (N=Length of String)
# When the order does matter it is a Permutation.
# Permutation Types -
# 	Repetation allowed - For a three digit lock, the repeat permutations are 10 X 10 X 10 = 1000 permutations
# 	No Repeat - For a three digit lock, the non-repeat permutations are 10 X 9 X 8 = 720 permutations
# 				4 things can be placed in 4! = 4 × 3 × 2 × 1 = 24 different ways

# Combination - When the order doesn't matter
# Types
# Repeat -
# Non-repeat - Such as lottery numbers (2,14,15,27,30,33) Order doesn't matter


# def permutations(elements):
#     if len(elements) <= 1:
#         yield elements
#         return
#     for perm in permutations(elements[1:]):
#         for i in range(len(elements)):
#             # nb elements[0:1] works in both string and list contexts
#             yield perm[:i] + elements[0:1] + perm[i:]
#
#
# print(list(permutations("ABC")))


# *******
# Python native permutations
from itertools import permutations
print(list(permutations("ABCD",3)))
# 4 X 3 X 2 = 24 permutations

# from itertools import combinations
# combinations([1, 2, 3], 2)
