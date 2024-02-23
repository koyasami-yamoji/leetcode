from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    return len(max(''.join(map(str, nums)).split('0')))

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))