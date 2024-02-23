from typing import List


def countKDifference(nums: List[int], k: int):
	return [(nums[i], nums[j]) for i in range(len(nums)) for j in range(i) if (nums[i] - nums[j] == k) or (nums[j] - nums[i] == k)]


print(countKDifference([1,2,2,1], 1))