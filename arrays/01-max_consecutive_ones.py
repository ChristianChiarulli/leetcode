def find_max_consecutive_ones(nums):

    counter = 0
    max_count = 0

    for num in nums:
        if num == 1:
            counter += 1
            max_count = max(max_count, counter)
        else:
            counter = 0
    return max_count


nums = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]

find_max_consecutive_ones(nums)
