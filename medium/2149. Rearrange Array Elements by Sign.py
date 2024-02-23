from typing import List


class Solution:
	def rearrangeArray(self, nums: List[int]) -> List[int]:
		pos = list(filter(lambda i: i > 0, nums))
		neg = list(filter(lambda i: i < 0, nums))
		res = []
		for i, j in zip(pos, neg):
			res.append(i)
			res.append(j)
		return res


print(rearrangeArray([3,1,-2,-5,2,-4]))