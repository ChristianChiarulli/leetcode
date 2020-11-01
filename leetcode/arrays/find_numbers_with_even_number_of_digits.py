# Given an array nums of integers,
# return how many of them contain an even number of digits.


def find_numbers(nums):

    count = 0

    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1

    return count


nums = [12, 345, 2, 6, 7896]

find_numbers(nums)
