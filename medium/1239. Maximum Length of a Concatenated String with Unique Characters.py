lst = ["cha","r","act","ers"]

first_max_len = 0
index = 0
second_max_len = 0

for i, word in enumerate(lst):
	if len(word) > first_max_len:
		index = i
		first_max_len = len(word)

lst.pop(index)

for i, word in enumerate(lst):
	if len(word) > second_max_len:
		second_max_len = len(word)


