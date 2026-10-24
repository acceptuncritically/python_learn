from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            presum[i+1]=nums[i]+presum[i]
        cache={}
        count=0
        for j,item in enumerate(presum):
            other=item-k
            if other in cache:
               count+=cache[other]
            cache[item]=cache.get(item,0)+1
        return count

