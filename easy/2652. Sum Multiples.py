# class Solution:
#     def sumOfMultiples(self, n: int) -> int:
#         return sum([i for i in range(1, n + 1) if (i % 3 == 0 or i % 5 == 0 or i % 7 == 0)])



def sumOfMultiples(n: int):
    summ_1 = 0
    summ_2 = [i for i in range(1, n) if any((i % 3 == 0, i % 5 == 0, i % 7 == 0))]

    for i in range(1, n):
        print(f'On start {summ_1=}')
        print(i)
        three = i % 3 == 0
        five = i % 5 == 0
        seven = i % 7 == 0

        if any((three, five, seven)):
            summ_1 += n
            print(f'{summ_1=}')

    print(f'sum1 = {summ_1}')
    print(f'sum2 = {summ_2}')


sumOfMultiples(7)