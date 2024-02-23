from typing import List


def arithmeticTriplets(nums: List[int], diff: int) -> int:
	# count = 0
	# for i in range(len(nums)):
	# 	for j in range(i):
	# 		for k in range(j):
	# 			if nums[i] - nums[j] == diff and nums[j] - nums[k] == diff:
	# 				count += 1
	return len([i for i in range(len(nums)) for j in range(i) for k in range(j) if nums[i] - nums[j] == diff and nums[j] - nums[k] == diff])


print(arithmeticTriplets([0,1,4,6,7,10], 3))