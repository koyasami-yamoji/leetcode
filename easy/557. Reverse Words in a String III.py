


def reverseWords(s: str) -> str:
	return ' '.join([''.join(reversed(list(i))) for i in s.split()])


print(reverseWords("hello world"))