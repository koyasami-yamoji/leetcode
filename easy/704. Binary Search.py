from typing import List

class Solution:
	def search(nums: List[int], target: int) -> int:
		left, right = 0, len(nums) - 1
		mid = (left + right) // 2

		while left <= right:
			if nums[mid] == target:
				return mid
			if nums[mid] < target:
				left = mid + 1
			elif nums[mid] > target:
				right = mid - 1

			mid = (left + right) // 2
		return -1


print(search([-1,0,3,5,9,12], 2))