from typing import List
import itertools


def findJudge(n: int, trust: List[List[int]]) -> int:
	trusted = set()
	for i in trust:
		trusted.add(i[0])
	return -1 if len(trusted) == n else list(trusted ^ set(range(1, n+1)))[0]

print(findJudge(2, [[1,2]]))