import heapq


class Solution:
    def minimizeSum(self, N, arr):
        heapq.heapify(arr)
        sum = 0
        while True:
            if len(arr) > 1:
                elm1 = heapq.heappop(arr)
                elm2 = heapq.heappop(arr)

                sum += elm1 + elm2
                heapq.heappush(arr, elm1 + elm2)
            else:
                break

        return sum



o = Solution()
str = "4 5 4 1 3 7 6 3 3"
lst = [int(x) for x in str.split(" ")]

# print(o.minimizeSum(len(lst), lst))

# [1, 4, 7, 10]
# 5 [5, 7, 10]
# 5 + 12 = 17 [12, 10]
# 17 + 22 = 39 [22]