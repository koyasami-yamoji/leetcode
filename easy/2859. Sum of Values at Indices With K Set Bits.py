from typing import List


def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
	return sum([nums[i] for i in range(len(nums)) if str(bin(i))[2:].count('1') == k])
