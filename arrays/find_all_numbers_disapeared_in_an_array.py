# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive
# that do not appear in this array.

# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


def find_disappeared_numbers(nums):

    hash_table = {}

    for num in nums:
        hash_table[num] = 1

    disap_nums = []
    
    print(hash_table)

    for i in range(1, len(nums) + 1):
        print(i)
        if i not in hash_table:
            print(i)
            disap_nums.append(i)
            print(disap_nums)

    return disap_nums


nums = [4, 3, 2, 7, 8, 2, 3, 1]

# nums = [1, 1]

find_disappeared_numbers(nums) #?
