# Given an array nums of integers,
# return how many of them contain an even number of digits.


def find_numbers_easy(nums):

    even_number_count = 0

    for num in nums:
        if len(str(num)) % 2 == 0:
            even_number_count += 1

    return even_number_count


def find_numbers_hard(nums):

    even_number_count = 0

    for num in nums:

        digit_count = 0
        while num > 0:
            digit_count += 1
            print(digit_count)
            num = num // 10  # normal integer division
            print(num)

        if digit_count % 2 == 0:
            even_number_count += 1

    return even_number_count


nums = [12, 345, 2, 6, 7896]

find_numbers_easy(nums)  # ?

find_numbers_hard(nums)  # ?
