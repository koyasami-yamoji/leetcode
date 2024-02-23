from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        while left <= right:
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            mid = (left + right) // 2
        return left


print(searchInsert([1,3,5,6],7))