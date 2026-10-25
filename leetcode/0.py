def subarrays_div_by_k(nums: list[int], k: int) -> int:
    seen = {0: 1}       # 余数 -> 出现次数，空前缀余数 0 出现过 1 次
    total = 0           # 当前前缀和
    count = 0           # 答案

    for x in nums:
        total += x
        r = total % k   # Python 负数取模自动非负
        count += seen.get(r, 0)   # 之前同余的前缀有几个，就新增几个合法子数组
        seen[r] = seen.get(r, 0) + 1
    return count