

def balancedStringSplit(s: str) -> int:
	balance = 0
	answer = []
	for i in s:
		if i == "L":
			balance += 1
		else:
			balance -= 1
		if balance == 0:
			answer += 1
	return answer


print(balancedStringSplit("RLRRLLRLRL"))