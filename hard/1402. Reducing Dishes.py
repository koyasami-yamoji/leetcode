from typing import List


def maxSatisfaction(satisfaction: List[int]) -> int:
	new_s = [x for x in satisfaction if x < -1]