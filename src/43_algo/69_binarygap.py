# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    results = {"0": 0}
    curr_pos = 0
    # checks
    # 1. Is the value numeric, if not exit with 0
    if (type(N) is not int):
        return 0

    # 2. If the value is lesser than 4, then there wont be any binary gap
    if N <= 4 or N >= 2147483647:
        return 0

    # convert int to bin and remove the first two chars. Eg: 529:int to bin 0b1000010001,
    # after first two char removed is 1000010001
    binVal = bin(N)[2:]

    # check if there is 1 present, and atleast should have 2 vals
    instance_count = binVal.count('1')

    # must have alteast two 1's
    if instance_count < 2:
        return 0

    # Implement your solution here
    while curr_pos < len(binVal):
        if binVal[curr_pos] == '1':
            nextPos = binVal.find('1', curr_pos+1)

            if nextPos == -1:
                break
            else:
                results[len(results)] = nextPos - (curr_pos+1)
                curr_pos = nextPos
        else:
            curr_pos += 1

    return max(results.values())


print(solution(529))
