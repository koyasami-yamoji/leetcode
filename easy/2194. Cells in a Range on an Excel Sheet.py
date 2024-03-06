from typing import List


class Solution:
	def cellsInRange(self, s: str) -> List[str]:
		result = [f'{chr(i)}{j}' for i in range(ord(s[0]), ord(s[-2]) + 1) for j in range(int(s[1]), int(s[-1])+1)]
		return result

print(cellsInRange("U7:X9"))