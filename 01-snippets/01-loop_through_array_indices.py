def snip(arr):
    indices = []
    values = []
    for i in range(len(arr)):
        indices.append(i)
        values.append(arr[i])

    return indices, values


arr = [1, 3, 2, 6]

print(snip(arr))
