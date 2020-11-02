# Given a sorted array nums, remove the duplicates
# in-place such that each element appears only once
# and returns the new length.

# Do not allocate extra space for another array,
# you must do this by modifying the input array
# in-place with O(1) extra memory.


def remove_elements(nums):

    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

remove_elements(nums)

nums
