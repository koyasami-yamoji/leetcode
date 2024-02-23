from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
	return len([i for i in range(len(words)) if all(j in allowed for j in words[i])])


print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))