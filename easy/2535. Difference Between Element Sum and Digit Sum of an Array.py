from typing import List


def differenceOfSum(nums: List[int]) -> int:
    return sum(nums) - sum(list(map(lambda num: int(num), ''.join([str(i) for i in nums]))))


print(differenceOfSum([1,15,6,3]))

def countDigits(num: int) -> int:
    return len([i for i in str(num) if num % int(i) == 0])