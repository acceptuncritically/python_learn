class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        slow=0
        fast=0
        total=0
        length=float('inf')
        while fast<len(nums):
            total+=nums[fast]
            while total>=target:
                #先更新长度在慢指针加1
                length=min(length,fast-slow+1)
                total-=nums[slow]
                slow+=1

            fast+=1
        return length if length!=float('inf') else 0
a=Solution()
b=a.minSubArrayLen(7,[2,3,1,2,4,3])
print(b)

