
class Solution:
	def isValid(self, s: str):
		stack = []
		for char in s:
			while len(stack) >= 3:
				if f"{stack[-3]}{stack[-2]}{stack[-1]}" == 'abc':
					for _ in range(3):
						stack.pop()
				else:
					break
			stack.append(char)
		if ''.join(stack) == 'abc':
			return True
		return False



print(isValid("aabcbc"))
