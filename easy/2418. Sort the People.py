from typing import List


def sortPeople(names: List[str], heights: List[int]) -> List[str]:
	return sorted(list(zip(names, heights)), key=lambda x: x[1], reverse=True)


print(sortPeople(["Mary","John","Emma"], [180,165,170]))