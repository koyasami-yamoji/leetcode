from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
	return sum([1 for i in sorted(nums) if sum(range(i))])
