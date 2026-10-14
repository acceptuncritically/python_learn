class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        # i 是快指针，遍历整个数组
        for i in range(len(nums)):
            # 当遇到非零元素时
            if nums[i] != 0:
                # 将非零元素交换到慢指针 j 的位置
                nums[i], nums[j] = nums[j], nums[i]
                # 慢指针向后移动一位，等待下一个非零元素
                j += 1