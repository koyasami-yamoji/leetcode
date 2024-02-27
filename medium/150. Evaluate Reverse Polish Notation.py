from typing import List

class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		operations = {
			'+': lambda x, y: x + y,
			'-': lambda x, y: x - y,
			'*': lambda x, y: x * y,
			'/': lambda x, y: x / y,
		}

		for token in tokens:
			if token[-1].isdigit():
				stack.append(int(token))
				continue
			second_num = stack.pop()
			first_num = stack.pop()
			stack.append(operations[token](first_num, second_num))

		return stack[-1]


print(evalRPN(["2","1","+","3","*"]))

