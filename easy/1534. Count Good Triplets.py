from typing import List


class Solution:
	def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
		return len([(arr[i], arr[j], arr[k])
					for i in range(len(arr))
					for j in range(i + 1, len(arr))
					if abs(arr[i] - arr[j]) <= a
					for k in range(j + 1, len(arr))
					if abs(arr[j] - arr[k]) <= b
					and abs(arr[i] - arr[k]) <= c])


print(countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
