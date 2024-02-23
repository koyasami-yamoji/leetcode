from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = [i for i in words if i == i[::-1]]
        if res:
            return res[0]
        return ''


print(firstPalindrome(["abc","car","ada","racecar","cool"]))