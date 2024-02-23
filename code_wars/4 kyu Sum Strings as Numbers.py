
import sys


def sum_strings(x: str, y: str):
	sys.set_int_max_str_digits(0)
	summ = 0
	if x:
		summ += int(hex(int(x)), base=16)
	if y:
		summ += int(hex(int(y)), base=16)

	return str(int)
sum_strings()