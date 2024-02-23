from typing import List

class Solution:
	def onesMinusZeros(self, grid: List[List[int]]):
		rows_count = len(grid)
		rows_len = len(grid[0])
		answ = [[0] * rows_len for _ in range(rows_count)]
		one_rows = [row.count(1) for row in grid]
		one_colmn = [row.count(1) for row in zip(*grid)]

		for i in range(rows_count):
			for j in range(rows_len):
				answ[i][j] = one_rows[i] + one_colmn[j] - (rows_len - one_rows[i]) - (rows_count - one_colmn[j])
		return answ


print(onesMinusZeros([
				[0, 1, 1], # [0][0] - 2 + 1 -
				[1, 0, 1],
				[0, 0, 1]
				]))