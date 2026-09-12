class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        length=len(heights)
        for i,a in enumerate(heights):
            f=a
            for j in range(length):
                if j==i:
                    continue
                vol=min(a,heights[j])*(j-i)
                if vol>res:
                    res=vol
        return res
                

