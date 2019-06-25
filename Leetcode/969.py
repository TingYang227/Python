class Solution(object):
    def pancakeSort(self, A):
        res = list()
        for i in range(len(A), 1, -1):
            idx = A.index(i) + 1
            A = A[:idx][::-1] + A[idx:]
            A = A[:i][::-1]
            res += [idx, i]
        return res