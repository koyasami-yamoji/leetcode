from typing import List


def decompressRLElist(nums: List[int]) -> List[int]:
	res = []
	
	for i in range(0, len(nums), 2):
		for j in range(nums[i]):
			res.append(nums[i + 1])
	res = [nums[i + 1] for i in range(0, len(nums), 2) for j in range(nums[i])]
	return res


print(decompressRLElist([1,1,2,3]))