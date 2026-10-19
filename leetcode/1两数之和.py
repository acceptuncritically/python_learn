"""
给定一个整数数组nums和一个整数目标值
target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
示例1：
输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：因为
nums[0] + nums[1] == 9 ，返回[0, 1] 。
示例2：
输入：nums = [3, 2, 4], target = 6
输出：[1, 2]
示例3：
输入：nums = [3, 3], target = 6
输出：[0, 1]
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}  # 字典：记录【元素值 : 索引】
        for i, num in enumerate(nums):
            # enumerate包含当前索引和当前数字，是内置的函数库
            complement = target - num  # 需要的另一个数
            # 判断补数是否在我们的字典里（说明前面遍历过）
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # 如果不在，把当前数和索引存进去，供后面的数匹配
            num_to_index[num] = i
        return []

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(0, len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
if __name__ == '__main__':
    s=Solution()
    result=s.twoSum([2, 7, 11, 15], 9)
    print(result)