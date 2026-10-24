class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
    #在这里面的变量相当于全局变量
    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left,right+1):
            total+=self.nums[i]
        return total
"""前缀和列表
"""
class NumArray1:
    def __init__(self, nums: list[int]):
        self.presum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.presum[i+1]=self.presum[i]+nums[i]
    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1]-self.presum[left]
if __name__=='__main__':
    a=NumArray1([-2,0,3,-5,2,-1])
    print(a.sumRange(2,5))
