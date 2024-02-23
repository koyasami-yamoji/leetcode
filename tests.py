def custom_filter(lst):
    return sum([int(i) for i in lst if isinstance(i, int) and i % 7 == 0]) < 83


print(custom_filter([7, 14, 28, 32, 32, '56']))