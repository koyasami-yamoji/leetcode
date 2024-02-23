from typing import List


def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
	return list(set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3))

print(twoOutOfThree([1,1,3,2], [2,3],[3]))