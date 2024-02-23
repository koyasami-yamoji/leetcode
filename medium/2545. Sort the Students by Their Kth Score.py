from typing import List


def sortTheStudents(score: List[List[int]], k: int):
	return sorted(score, key=lambda x: x[k], reverse=True)


print(sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], k=2))