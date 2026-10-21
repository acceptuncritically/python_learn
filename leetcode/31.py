def nextPermutation(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    i=n-2
    while i>=0 and nums[i]>=nums[i+1]:
        i-=1
    j=n-1
    while j>=0 and nums[i]>=nums[j]:
        j-=1
    nums[j],nums[i]=nums[i],nums[j]
    left,right=i+1,n-1
    while left!=right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1





