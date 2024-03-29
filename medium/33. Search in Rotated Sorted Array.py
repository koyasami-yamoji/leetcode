from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = (right + left) // 2
			if nums[mid] == target:
				return mid
			elif nums[left] <= nums[mid]:
				if nums[left] <= target <= nums[mid]:
					right = mid - 1
				else:
					left = mid + 1
			elif nums[mid] <= target <= nums[right]:
				left = mid + 1
			else:
				right = mid - 1
		return -1


print(search([5,1,3], 3))
print(search([4,5,6,7,8,1,2,3], 2))
# print(search([4,5,6,7,0,1,2], 0))