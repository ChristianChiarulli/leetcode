# Given a binary array, find the maximum number of consecutive

# 1s in this array if you can flip at most one 0.


def find_max_consecutive_ones(nums):

    prevCount = currCount = maxCount = plus = 0

    for num in nums:
        if num == 0:
            maxCount = max(maxCount, prevCount + currCount)
            prevCount = currCount
            currCount = 0
            plus = 1
        currCount += num
    maxCount = max(maxCount, prevCount + currCount)
    return maxCount + plus
