
def countSubstrings(s: str):
	res = []
	for i in range(len(s)):
		for j in range(len(s)):
			word = s[i:j] if j != 0 else s[:1]
			if word == word[::-1]:
				res.append(word)
	return res

print(countSubstrings("aaa"))