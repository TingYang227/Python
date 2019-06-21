# Input: [3,2,3,4]
# Output: 10

class Solution:
    def largestPerimeter(self, A):
        # sort the list according to descending order
        A_sorted = sorted(A, reverse=True)

        Perimeter = 0
        for i in range(len(A_sorted)-2):
            if A_sorted[i] < A_sorted[i+1] + A_sorted[i+2]:
                Perimeter = sum(A_sorted[i:i+3])
                return Perimeter
            else:
                pass

        return Perimeter


# Runtime: 56 ms, faster than 99.72%
# list.sort() seems to be faster than sorted(list)
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # sort the list according to descending order
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
            else:
                pass

        return 0



if __name__ == "__main__":
    test = Solution()
    alist = [1,2,1]
    print(test.largestPerimeter(alist))


