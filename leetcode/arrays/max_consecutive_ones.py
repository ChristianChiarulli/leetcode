def find_max_consecutive_ones(nums):

    counter = max_count = 0

    for num in nums:
        if num == 1:
            counter += 1
            max_count = max(counter, max_count)
        else:
            counter = 0

    return max_count


nums = [1, 1, 1, 0, 1]

find_max_consecutive_ones(nums)
