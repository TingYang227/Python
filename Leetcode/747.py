class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = 0

        for i in range(len(nums)):
            if nums[max_index] <= nums[i]:
                max_index = i

        for i in range(len(nums)):
            if (max_index != i) and (nums[max_index] < nums[i] * 2):
                return -1

            return max_index







nums = [1, 0, 6, 3]
a = Solution()

print(a.dominantIndex(nums))


