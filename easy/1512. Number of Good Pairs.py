
def numIdenticalPairs(nums: list[int]):
	"""
	:type nums: List[int]
	rtype: int
	"""
	return len([[i, j] for i in range(len(nums)) for j in range(i) if nums[i] == nums[j]])


print(numIdenticalPairs([1,2,3,1,1,3]))