# Given an array arr of integers, check if there exists
# two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

_i = []
_num = []


def check_if_exist(arr):

    if arr[0] == 0 and arr[1] == 0:
        return True

    my_dict = {}

    for num in arr:
        my_dict[2 * num] = None

    for num in arr:
        if num in my_dict.keys() and num != 0:
            return True

    return False


# arr = [-2, 0, 10, -19, 4, 6, -8]
arr = [-2, 0, 10, -19, 4, 6, -8]
# arr = [10, 0, 5, 3]
# arr = [0, 0]

check_if_exist(arr)

_i
_num

my_dict = {}

my_dict[2 * 6] = True

my_dict

12 in my_dict.keys()

True in my_dict.values()
