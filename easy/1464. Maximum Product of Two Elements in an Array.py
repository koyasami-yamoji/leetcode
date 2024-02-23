from typing import List


def maxProduct(nums: List[int]):
	return max([(nums[i] - 1) * (nums[j] - 1) for j in range(len(nums)) for i in range(len(nums) - 1) if i != j])



print(maxProduct([3, 4, 5, 2]))

# Input: nums = [3, 4, 5, 2]
# Output: 12

# i = 1 and j = 2(indexed

# maximum
# value, that is, (nums[1] - 1) * (nums[2] - 1) = (4 - 1) * (5 - 1) = 3 * 4 = 12.