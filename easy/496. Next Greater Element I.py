from typing import List


class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		res = {}
		stack_nums2 = []
		for i, value in enumerate(nums2):
			while stack_nums2 and nums2[stack_nums2[-1]] < value:
				res[nums2[stack_nums2.pop()]] = value
			stack_nums2.append(i)
		return [res.get(i, -1) for i in nums1]



# The problem says, there are two arrays, nums1 and nums2.
# What we have to do is, we have to traverse in nums1 and for
# each element of the nums1 we have to:
# a) find the current element of nums1 in nums2
# b) find the next greater element of that element in nums2
# c) store that greater element in a vector
# d) return the vector.