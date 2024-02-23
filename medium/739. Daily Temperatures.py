from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answ = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                answ[index] = i - index
            stack.append(i)
        return answ

print(dailyTemperatures([73,74,75,71,69,72,76,73]))


# [1,1,4,2,1,1,0,0]