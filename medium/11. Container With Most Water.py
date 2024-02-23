from typing import List

class Solution:
	def maxArea(self, height: List[int]) -> int:
		low = 0
		high = len(height) - 1
		maxx = 0
		while low < high:
			left = height[low]
			right = height[high]
			if left > right:
				maxx2 = right * (high - low)
				if maxx2 > maxx:
					maxx = maxx2
				high -= 1
			elif left <= right:
				maxx2 = left * high
				if maxx2 > maxx:
					maxx = maxx2
				low += 1

		return maxx


print(maxArea([4,3,2,1,4]))