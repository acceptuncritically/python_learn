# def twoSum(numbers: list[int], target: int) -> list[int]:
#     for i in range(0, len(numbers)):
#         for j in range(i, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 break
#         break
#     return [i+1, j+1]
from typing import List


#哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i,item in enumerate(nums):
            if target-item in cache:
                return [cache[target-item]+1,i+1]
            cache[item] = i
a=Solution()
res=a.twoSum([2,7,11,15],9)
print(res)