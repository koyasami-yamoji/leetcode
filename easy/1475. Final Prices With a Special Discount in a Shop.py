from typing import List

class Solution:
	def finalPrices(self, prices: List[int]) -> List[int]:
		stack = []
		for i, price in enumerate(prices):
			while stack and prices[stack[-1]] >= price:
				index = stack.pop()
				prices[index] = prices[index] - prices[i]
			stack.append(i)
		return prices


print(finalPrices([8,4,6,2,3]))