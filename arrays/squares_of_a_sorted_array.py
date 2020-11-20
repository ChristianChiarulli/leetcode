# Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number,
# also in sorted non-decreasing order.


def sorted_squares(nums):

    return sorted(i ** 2 for i in nums)


nums = [-4, -1, 0, 3, 10]
print(nums)

sorted_squares(nums)

