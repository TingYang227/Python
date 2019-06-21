# 第一次我自己的解法，速度太慢

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # find the shorter one

        intersec = []
        set1 = set(nums1)
        set2 = set(nums2)
        if (len(set1) < len(set1)):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]


# 网上答案
"""
class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
"""