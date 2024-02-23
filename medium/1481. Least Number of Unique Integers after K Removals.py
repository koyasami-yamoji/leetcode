import collections
from typing import List

class Solution:
	def findLeastNumOfUniqueInts(self, arr: List[int], k: int):
		res = sorted(collections.Counter(arr).values())
		count = 0
		for j, num in enumerate(res):
			if k > res[j]:
				k -= res[j]
				res[j] = 0
			else:
				res[j] -= k
				k = 0
			if res[j] > 0:
				count += 1
		return count


print(findLeastNumOfUniqueInts(
	[24, 119, 157, 446, 251, 117, 22, 168, 374, 373, 323, 311, 441, 213, 120, 412, 200, 236, 328, 24, 164, 104, 331, 32,
	 19, 223, 89, 114, 152, 82, 456, 381, 355, 343, 157, 245, 443, 368, 229, 49, 82, 16, 373, 142, 240, 125, 8], 41))
