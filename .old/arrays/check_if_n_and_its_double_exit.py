# Given an array arr of integers, check if there exists
# two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

_i = []
_num = []


def check_if_exist(arr):

    if arr.count(0) > 1:
        return True

    s = set()

    for num in arr:
        s.add(2 * num)

    for num in arr:
        if num in s and num != 0:
            return True

    return False


# arr = [-2, 0, 10, -19, 4, 6, -8]
# arr = [-2, 0, 10, -19, 4, 6, -8]
# arr = [10, 0, 5, 3]
# arr = [0, 0]
arr = [2, 3, 3, 0, 0]

check_if_exist(arr)

_i
_num

my_dict = {}

my_dict[2 * 6] = True

my_dict

12 in my_dict.keys()

True in my_dict.values()
