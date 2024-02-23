from typing import List


def uncommonFromSentences(s1: str, s2: str) -> List[str]:
    s1 = s1.split()
    s2 = s2.split()
    return list(set([i for i in s1 if s1.count(i) == 1 and s2.count(i) < 1]).symmetric_difference(
        set([i for i in s2 if s2.count(i) == 1 and s1.count(i) < 1])))


print(uncommonFromSentences("this apple is sweet", "this apple is sour"))

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        return list(set([i for i in s1 if s1.count(i) == 1 and s2.count(i) < 1]).symmetric_difference(
        	set([i for i in s2 if s2.count(i) == 1 and s1.count(i) < 1])))