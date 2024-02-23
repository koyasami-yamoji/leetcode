from typing import List

class Solution:
	def findMatrix(self, nums: List[int]):
		result = [list(set(nums))]
		nums1 = nums
		for num in result[-1]:
			nums1.remove(num)

		if nums1:
			result, nums = self.delete_set_nums(result, nums1)

		return result

	def delete_set_nums(self, result, nums):
		result.append(list(set(nums)))
		for num in result[-1]:
			if num in nums:
				nums.remove(num)
		if nums:
			self.delete_set_nums(result, nums)
		return result, nums


print(findMatrix([2,3,1]))