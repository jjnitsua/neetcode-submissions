class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=defaultdict(int)
        maxl=0
        l=0
        if len(s)<=1:
            return len(s)
        while l<len(s):
            if s[l] in m:
                l=m[s[l]]+1
                maxl=max(maxl,len(m))
                m={}
            else:
                m[s[l]]=l
                l+=1
                maxl=max(maxl,len(m))
        return maxl

        