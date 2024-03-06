from collections import deque

class Solution:
	def minimumLength(s: str) -> int:

		left = 0
		right = len(s)-1
		deque_string = deque(s)

		for _ in range(len(s)):
			if len(deque_string) == 1:
				return 1
			elif deque_string and deque_string[0] != deque_string[-1]:
				return len(deque_string)
			elif not deque_string:
				return len(deque_string)

			char = deque_string[0]

			while True:
				if deque_string and char == s[left]:
					deque_string.popleft()
					left += 1
				else:
					break

			while True:
				if deque_string and char == s[right]:
					deque_string.pop()
					right -= 1
				else:
					break

		return len(deque_string)


print(minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))