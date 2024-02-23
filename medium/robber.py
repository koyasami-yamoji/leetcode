from typing import List


def rob(nums: List[int]) -> int:
	prev1 = 0  # dp[i - 1]
	prev2 = 0  # dp[i - 2]

	for num in nums:
		dp = max(prev1, prev2 + num)
		prev2 = prev1
		prev1 = dp

	return prev1


print(rob([2, 3, 4, 5, 6]))
