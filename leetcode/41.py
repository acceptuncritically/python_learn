def maxSubArray(nums: list[int]) -> int:
    list1 = []
    for low in range(0, len(nums)):
        for fast in range(low, len(nums)):
            list1.append(nums[low:fast])

    if not any(list1):
        return sum(nums)
    else:
        return max(sum(i) for i in list1)
a=maxSubArray([1])
print(a)
