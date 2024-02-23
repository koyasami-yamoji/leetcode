from typing import List

class Solution:
	def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
		nums = sorted(nums)
		res = []
		for i in range(0, len(nums), 3):
			if nums[i + 1] - nums[i] <= k and nums[i + 2] - nums[i] <= k:
				res.append([nums[i], nums[i+1], nums[i + 2]])
			else:
				return []
		return res


print(divideArray([1,3,3,2,7,3], 2))