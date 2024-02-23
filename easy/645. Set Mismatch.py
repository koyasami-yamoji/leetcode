class Solution:
	def findErrorNums(self, nums: list[int]):
		n = len(nums)
		expected_sum = n * (n + 1) / 2
		duplicated_number = [num for num in nums if nums.count(num) > 1]
		missing_number = expected_sum - (sum(nums) - duplicated_number[0])
		return [duplicated_number[0], int(missing_number)]


print(findErrorNums([2,2]))



# expectedSum = n * (n+1) / 2.
# missing number = expectedSum - (actualSum - duplicatedNumber).