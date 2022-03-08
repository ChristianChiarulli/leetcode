def third_max(nums):

    nums = set(nums)

    max_val = max(nums)

    if len(nums) < 3:
        return max_val

    for _ in range(2):
        nums.remove(max_val)
        max_val = max(nums)

    return max(nums)


nums = [3, 2, 1]

third_max(nums)

