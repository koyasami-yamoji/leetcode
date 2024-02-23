from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            for j in range(arr1.count(i)):
                result.append(i)
                arr1.remove(i)
        return result + sorted(arr1)


print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))