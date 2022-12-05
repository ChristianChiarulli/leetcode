
def two_sum(nums, target):
    map = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [map[diff], i]
        map[n] = i
