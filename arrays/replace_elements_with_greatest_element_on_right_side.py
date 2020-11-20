def replace_elements(arr):

    max_val = arr[-1]
    temp = 0

    for i in range(len(arr) - 1, 0, -1):

        max_val = max(temp, max_val)
        temp = arr[i - 1]
        arr[i - 1] = max_val

    arr[-1] = -1


arr = [17, 18, 5, 4, 6, 1]

replace_elements(arr)

arr

expected_output = [18, 6, 6, 6, 1, -1]

assert arr == expected_output
