from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
	q = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
	return [q[i][0] for i in range(k)]

print(topKFrequent([1,1,1,2,2,3], 2))