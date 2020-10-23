high_arr = []
low_arr = []
mid_arr = []
value_arr = []


def binary_search(data, target, low, high):
    high_arr.append(high)
    low_arr.append(low)

    if low > high:
        return False  # interval is empty, no match
    else:
        mid = (low + high) // 2  # floor divsion
        mid_arr.append(mid)
        value_arr.append(data[mid])
        if target == data[mid]:  # found a match
            return mid
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


# input array (sorted)
arr = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

# Remember 0 - 15 are the indexes
len(arr)

binary_search(arr, 22, 0, 15)

high_arr
low_arr
mid_arr
value_arr
