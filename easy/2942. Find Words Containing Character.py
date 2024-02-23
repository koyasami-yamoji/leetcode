from typing import List


def countPairs(self, nums: List[int], target: int) -> int:
	return len([(i, j) for i in range(len(nums)) for j in range(i) if 0 <= i < j < len(nums) and nums[i] + nums[j] < target])
