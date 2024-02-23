from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
	return [len([j for j in range(len(nums)) if i > nums[j]]) for i in nums]


print(smallerNumbersThanCurrent([8,1,2,2,3]))