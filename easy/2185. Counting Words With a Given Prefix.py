from typing import List


def prefixCount(words: List[str], pref: str) -> int:
	return sum([1 for i in words if i.startswith(pref)])


print(prefixCount(["pay","attention","practice","attend"], 'at'))