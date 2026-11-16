class Solution:
    #哈希表
    def haxi(self,nums,target):
        cache={}
        for i,item in enumerate(nums):
            if target - item in nums:
                return [nums.index(target),i]
            cache[item]=i


    #滑动窗口
    def sliding_window_algorithm(self,nums, target):
        #要保证全是同是正数或负数保证加减时不会错误
        slow,fast=0,0
        total=0
        length = float("inf")
        while fast<len(nums):
            total+=nums[fast]
            while total>=target:
                length=min(length,fast-slow+1)
                total-=nums[slow]
                slow+=1
            fast+=1
        return length if length!=float("inf") else 0


    #前缀和
    def subarrays_div_by_k(self,nums: list[int], k: int) -> int:
        pre_sum=[0]*(len(nums)+1)
        count=0
        for i,item in nums:
            pre_sum[i]=pre_sum[i-1]+item


    # #差分数组
    # def
if __name__=="__main__":
    a=Solution()
    print(a.sliding_window_algorithm([2,3,1,2,4,3],7))