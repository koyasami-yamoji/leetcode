import math


def subtractProductAndSum(n: int) -> int:
    x = sum([int(i) for i in str(n)])
    y = math.prod(list(map(lambda q: int(q), list(str(n)))))
    return math.prod(list(map(lambda q: int(q), list(str(n))))) - sum([int(i) for i in str(n)])
    print(x)
    print(y)

subtractProductAndSum(234)