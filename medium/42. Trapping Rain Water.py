from typing import List


def trap(height: List[int]) -> int:
	max_num_index = height.index(max(height))
	count = 0
	for i in range(max_num_index, len(height)):
