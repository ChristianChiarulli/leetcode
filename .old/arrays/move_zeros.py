# gotta remove traverse from the end


def move_zeros(nums):

    zero_count = nums.count(0)

    for i in range(len(nums) - 1, -1, -1):
        if zero_count > 0 and nums[i] == 0:
            del nums[i]
            nums.append(0)
            zero_count -= 1


nums = [0, 1, 0, 3, 12]

nums.count(0)

move_zeros(nums)

nums

