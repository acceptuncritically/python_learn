class Solution:
    def search(self, nums: list[int], target: int) -> int:
        import math
        if target not in nums:
            return -1
        mid=math.ceil(len(nums)/2)
        while True:
            if target>nums[mid]:
                mid=math.ceil(len(nums[mid+1:]))/2
            elif target<nums[mid]:
                mid=math.ceil(len(nums[:mid-1]))/2
            else:
                return mid