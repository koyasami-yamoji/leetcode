class Solution:
	def maximum69Number(self, num: int) -> int:
		maxx = num
		for i in range(len(str(num))):
			if str(num)[i] == '6':
				kek = int(str(num)[:i] + '9' + str(num)[i + 1:])
				if kek > maxx:
					maxx = kek
			else:
				kek = int(str(num)[:i] + '6' + str(num)[i + 1:])
				if kek > maxx:
					maxx = kek
		return maxx


print(maximum69Number(9669))