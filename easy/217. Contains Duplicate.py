from typing import List


def containsDuplicate(nums: List[int]) -> bool:
	return sorted(list(set(nums))) != sorted(nums)


print(containsDuplicate([1,5,-2,-4,0]))