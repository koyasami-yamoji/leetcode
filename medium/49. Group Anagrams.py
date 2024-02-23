from typing import List
import re

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            ann = res.get(sorted_word)
            if ann:
                res[sorted_word].append(word)
            else:
                res[sorted_word] = [word]
        return [value for value in res.values()]

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]