from typing import List


def generate(numRows: int) -> List[List[int]]:
	res = [[1]]

	for i in range(1, numRows):
		summ = 1
		for j in range(i):
			summ *= 11
		res.append([int(num) for num in list(str(summ))])
	return res


print(generate(5))




# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] хуйня не решено