

digits = [4,3,2,9]

res = list(map(lambda y: int(y), str(int(''.join(list(map(lambda x: str(x), digits)))) + 1)))

print(res)