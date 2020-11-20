# Students are asked to stand in non-decreasing
# order of heights for an annual photo.

# Return the minimum number of students that must
# move in order for all students to be standing in
# non-decreasing order of height.

# Notice that when a group of students is selected
# they can reorder in any possible way between themselves
# and the non selected students remain on their seats.


def heightchecker(heights):

    swap_count = 0
    sorted_heights = sorted(heights)
    if heights == sorted_heights:
        return swap_count
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            swap_count += 1
    return swap_count


heights = [1, 1, 4, 2, 1, 3]

heightchecker(heights)
