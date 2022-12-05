
def contains_duplicate(nums):

    unique_nums = set()

    for num in nums:

        if num in unique_nums:
            return False

        unique_nums.add(num)

    return True

