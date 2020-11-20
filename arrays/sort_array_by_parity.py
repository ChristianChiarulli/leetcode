# Given an array A of non-negative integers,
# return an array consisting of all the even elements of A,
# followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.


def sort_array_by_parity(A):
    A.sort(key=lambda x: x % 2)
    return A


A = [7, 1, 3, 2, 4, 5]

sort_array_by_parity(A)
