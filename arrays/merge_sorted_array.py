# Given two sorted integer arrays nums1 and nums2,
# merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1
# and nums2 are m and n respectively.
# You may assume that nums1 has enough space
# (size that is equal to m + n) to hold additional elements from nums2.


def merge(nums1, m, nums2, n):
    print("fuck you")
    nums1[:] = sorted(nums1[:m] + nums2)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [1, 2, 5, 6]
n = 4

merge(nums1, m, nums2, n)

print(nums1)
