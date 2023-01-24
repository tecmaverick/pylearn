from collections import Counter


class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    # def isAnagram(a, b):
    #     if a is None and b is None:
    #         return True
    #
    #     if a is None or b is None:
    #         return False
    #
    #     a_dict = Counter(a)
    #     b_dict = Counter(b)
    #
    #     flaga = all([a_dict[x] == b_dict[x] for x in a_dict])
    #     flagb = all([a_dict[x] == b_dict[x] for x in b_dict])
    #     return all([flaga, flagb])

    # Sorting is still O(n lg n), you can find anagrams in O(n) with a dictionary
    def isAnagram(a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        return sorted(a) == sorted(b)

    def isAnagram1(a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False
        {}
        return sorted(a) == sorted(b)