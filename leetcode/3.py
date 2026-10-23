class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow=0
        fast=0
        length=0
        my_set=set()
        while fast<len(s):
            if s[fast] in my_set:
                my_set.remove(s[slow])
                slow+=1
            else:
                my_set.add(s[fast])
                length=max(length,len(my_set))
                fast+=1
        return length
