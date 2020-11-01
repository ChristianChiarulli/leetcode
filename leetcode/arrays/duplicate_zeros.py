# Given a fixed length array arr of integers,
# duplicate each occurrence of zero,
# shifting the remaining elements to the right.

# Note that elements beyond the length of the
# original array are not written.

# Do the above modifications to the input array in place,
# do not return anything from your function.

# remember len(arr) will return number of elements
# len(arr) - 1 will return final index

# solution by rombai


def duplicate_zeros(arr):

    capacity = len(arr)

    i = 0

    while i < capacity:
        if arr[i] == 0:
            del arr[len(arr) - 1]
            arr.insert(i, 0)
            i += 2  # so that you skip the 0 you just added
            continue
        else:
            i += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]

duplicate_zeros(arr)

arr
