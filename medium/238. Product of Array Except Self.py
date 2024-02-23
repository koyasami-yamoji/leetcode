from typing import List
from math import prod
from collections import defaultdict


def productExceptSelf(nums: List[int]) -> List[int]:
	result = []
	hashmap = defaultdict(int)
	for i in range(len(nums)):
		k = hashmap[nums[i]]
		if k == 0:
			nums1 = nums[:]
			nums1.pop(i)
			m = prod(nums1)
			hashmap[nums[i]] = m
			result.append(m)
		else:
			result.append(k)
	return result

print(productExceptSelf([1,2,3,4]))