from typing import List



def twoSum(numbers: List[int], target: int) -> List[int]:
	low = 0
	high = len(numbers) - 1
	while low < high:
		if numbers[low] + numbers[high] < target:
			low += 1
		elif numbers[low] + numbers[high] > target:
			high -= 1
		if numbers[low] + numbers[high] == target:
			break

	return [low+1, high+1]


print(twoSum([2,3,4], 6))