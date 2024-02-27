class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		key = {
			"}": "{",
			")": "(",
			"]": "["
		}
		for sym in s:
			if sym in '{[(':
				stack.append(sym)
			elif sym in "}])" and stack:
				if stack[-1] == key[sym]:
					stack.pop()
				else:
					return False
			else:
				return False
		if stack:
			return False
		return True