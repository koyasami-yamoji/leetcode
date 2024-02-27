
class Solution:
	def makeGood(self,s: str) -> str:
		stack = []
		for char in s:
			if stack and ord(char) - ord(stack[-1]) in [-32, 32]:
				stack.pop()
			else:
				stack.append(char)
		return ''.join(stack)

print(makeGood('leEeetcode'))