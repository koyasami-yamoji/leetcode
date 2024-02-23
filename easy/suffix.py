from typing import List



def longestCommonPrefix(strs: List[str]) -> str:
	res = ''
	for i in range(len(strs[0])):
		sym = strs[0][i]
		for word in strs:
			try:
				if word[i] == sym:
					continue
				else:
					return res
			except IndexError:
				return res
		res += sym
	return res


print(longestCommonPrefix(["ab", "a"]))
