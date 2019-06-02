class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            if left != right and (left + 1) == (right - 1):
                if left_sum > right_sum:
                    right_sum = right + nums[right]
                    right = right - 1
                else:
                    left_sum = left_sum + nums[i]
                    left = left + 1

        if left_sum == right_sum:
            return left+1

        return -1
