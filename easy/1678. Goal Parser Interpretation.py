

class Solution:
	def interpret(self, command: str) -> str:
		res = ''
		for i, char in enumerate(command):
			try:
				if char == '(' and command[i+1] == ')':
					res += 'o'
				elif char == ')' and command[i + 1] != ')' or char == '(':
					continue
				else:
					res += char
			except IndexError:
				if char == '(' or char == ')':
					break
				else:
					res += char
		return res



num = 526

print(int(str(int(str(num)[::-1]))[::-1]) == num)