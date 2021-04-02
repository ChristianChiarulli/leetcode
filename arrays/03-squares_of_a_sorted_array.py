# Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number,
# also in sorted non-decreasing order.


def sorted_squares_easy(nums):
    return sorted(i ** 2 for i in nums)


def sorted_squares_hard(nums):
    n = len(nums)
    result = []
    left_pointer = 0  # ?
    right_pointer = n - 1  # ?
    for _ in range(n - 1, -1, -1):  # remember start (inclusive) stop(exclusive) step

        if abs(nums[left_pointer]) < abs(nums[right_pointer]):
            num = nums[right_pointer]
            right_pointer -= 1
        else:
            num = nums[left_pointer]
            left_pointer += 1

        result.insert(0, num ** 2)
    return result


nums = [-40, -1, 0, 3, 10]

print(nums)

sorted_squares_easy(nums)  # ?

sorted_squares_hard(nums)  # ?
