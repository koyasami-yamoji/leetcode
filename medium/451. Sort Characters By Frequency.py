class Solution:
	def frequencySort(self, s: str):
		res = {}
		for char in set(s):
			res[char] = s.count(char)
		return ''.join([char * i for char, i in sorted(res.items(), key=lambda x: x[1], reverse=True)])

print(frequencySort("loveleetcode"))
