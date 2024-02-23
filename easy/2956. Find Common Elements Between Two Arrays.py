from typing import List


class Solution:
    def findIntersnctionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        left = sum([1 for i in range(len(nums1)) if nums1[i] in nums2])
        right = sum([1 for i in range(len(nums2)) if nums2[i] in nums1])
        return [left, right]