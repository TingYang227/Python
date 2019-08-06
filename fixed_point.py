A = [-10, -5, 2, 3, 4]

"""
def fixed_point(A):
    left = 0
    right = len(A) - 1

    while left < right:
        m = left + (right - left) // 2
        if A[m] - m < 0:
            left = m + 1
        else:
            right = m

    return left if A[left] == left else -1
"""


def fixedPoint(A):
    B = []
    for i in range(len(A)):
        if A[i] == i:
            B.append(i)
    if len(B) == 0:
        return -1
    else:
        return min(B)

print(fixedPoint(A))