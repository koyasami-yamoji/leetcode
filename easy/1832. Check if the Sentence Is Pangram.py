

def checkIfPangram(sentence: str) -> bool:
	lett = {}
	for i in sentence:
		lett[i] = 1
	if len(lett.keys()) == 26:
		return True
	return False
