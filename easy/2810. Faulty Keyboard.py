

class Solution:
	def finalString(seldf, s: str) -> str:
		res = ''
		for i in s:
			if i == 'i':
				res = res[::-1]
			else:
				res += i
		return res



print(finalString("string"))