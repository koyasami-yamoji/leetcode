
class Solution:
	def sortSentence(self, s: str) -> str:
		answer = [0] * len(s.split())
		for word in s.split():
			i = int(word[-1])
			answer[i - 1] = word[:-1]
		return ' '.join(answer)







print(sortSentence("is2 sentence4 This1 a3"))
# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort
# the
# words in s
# to
# their
# original
# positions
# "This1 is2 a3 sentence4", then
# remove
# the
# numbers.
# Example
# 2: