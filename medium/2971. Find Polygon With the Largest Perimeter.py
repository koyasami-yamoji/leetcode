from typing import List

class Solution:
	def largestPerimeter(self, nums: List[int]) -> int:
		summ = sum(nums)
		for i in sorted(nums, reverse=True):
			summ -= i
			if summ > i:
				return summ + i
		return -1


print(largestPerimeter([1, 1, 2, 3, 5, 12, 50]))


qwe = (1, 2)

