from typing import List


def removeDuplicates(nums: List[int], val):
	for num in nums:
		if num == val:
			nums.remove(val)
	print(nums)
	return len(nums)


print(removeDuplicates([1,2,2], 2))