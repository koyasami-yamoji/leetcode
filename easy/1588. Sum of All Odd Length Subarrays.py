from typing import List


def sumOddLengthSubarrays(arr: List[int]):
	# return [arr[:i] for i in range(len(arr) + 1) if i % 2 != 0]
	# summ = 0
	# for i in range(len(arr) + 1):
	# 	for j in range(len(arr) + 1):
	# 		if len(arr[i:j]) % 2 != 0:
	# 			summ += sum(arr[i:j])
	# print(summ)

	return sum([sum(arr[i:j]) for j in range(len(arr) + 1) for i in range(len(arr) + 1) if len(arr[i:j]) % 2 != 0])


print(sumOddLengthSubarrays([1,4,2,5,3]))

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
# Example 2: