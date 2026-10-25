class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        i=0
        cur = intervals[i]
        while i<len(intervals)-1:
            next=intervals[i+1]
            if cur[1]<=next[0]:
                cur[1]=max(next[1],cur[1])
            else:
                res.append(cur)
                cur=next
            i+=1
        return res