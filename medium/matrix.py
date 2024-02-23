
def minFallingPathSum(self, matrix: list) -> int:
	n = len(matrix)
	for r in range(1, n):
		for c in range(n):
			mid = matrix[r - 1][c]
			left = matrix[r - 1][c - 1] if c > 0 else float('inf')
			right = matrix[r - 1][c + 1] if c < n - 1 else float('inf')
			matrix[r][c] = matrix[r][c] + min(mid, left, right)
	return min(matrix[-1])


print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))

