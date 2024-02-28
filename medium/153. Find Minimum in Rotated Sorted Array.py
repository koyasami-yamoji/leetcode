from typing import List

class Solution:
	def findMin(self, nums: List[int]) -> int:
		low = 0
		high = len(nums) - 1
		mid = (low + high) // 2

		while low < high:
			if nums[mid] > nums[mid+1]:
				return nums[mid + 1]
			elif nums[mid] < nums[mid-1]:
				return nums[mid]
			elif nums[mid] > nums[high]:
				low = mid + 1
			elif nums[mid] < nums[high]:
				high = mid - 1
			mid = (low + high) // 2
		return nums[low]


print(findMin([3,4,5,1,2]))