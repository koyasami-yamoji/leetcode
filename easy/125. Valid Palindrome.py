
class Solution:
	def isPalindrome(self, s: str) -> bool:
		valid_text = ''.join([i for i in s.lower() if i.isalpha()])
		return valid_text == valid_text[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))