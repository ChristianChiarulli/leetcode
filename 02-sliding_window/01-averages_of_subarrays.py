def find_averages_of_subarrays(K, arr):

    result = []

    window_sum = 0

    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        # when the window end is greater than K start removing the first element and appending values
        if window_end >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1

    return result


result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])

print(result)
