
class Solution:
	def maxLengthBetweenEqualCharacters(self, s: str) -> int:
		max_dis = -1

		for left in range(len(s)):
			for right in range(left+1, len(s)):
				if s[left] == s[right]:
					max_dis = max(max_dis, right - left - 1)
		return max_dis


print(maxLengthBetweenEqualCharacters("abca"))