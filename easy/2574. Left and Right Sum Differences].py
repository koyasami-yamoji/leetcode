from typing import List

# not solved
def leftRightDifference(nums: List[int]) -> List[int]:
	# left_sum = [0] + nums[:len(nums) // 2 + 1]
	# left_sum_lst = [sum(left_sum[:i]) for i in range(1, len(left_sum) + 1)]
	# right_sum = nums[1:] + [0]
	# right_sum_lst = [sum(right_sum[i:]) for i in range(len(right_sum))]

	left_sum = []
	right_sum = []
	for i in range(len(nums)):
		for k in range(0, i - 1):
			left_sum.append(nums[k])
		else:
			left_sum.append(0)

		for j in range(i + 1, len(nums) - 1):
			right_sum.append(nums[j])
		else:
			right_sum.append(0)

	print(left_sum)
	print(right_sum)

	# return [i - j if i - j >= 0 else j - i for i, j in zip(left_sum_lst, right_sum_lst)]


print(leftRightDifference([10,4,8,3]))

#Iterate on the range j: [0 … i - 1] and
# dd nums[j] to the leftSum and similarly iterate on the range j
# : [i + 1 … nums.length - 1] and add nums[j] to the rightSum.
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# [	0 10,4,8,3]
# [0,10,14,22]
# [15,11,3,0]
#Iterate on the range j: [0 … i - 1] and
# dd nums[j] to the leftSum and similarly iterate on the range j
# : [i + 1 … nums.length - 1] and add nums[j] to the rightSum.
#