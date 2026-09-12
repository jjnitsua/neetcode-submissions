class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lMax,rMax=0,0
        area=0
        while l<r:
            if height[l]>lMax:
                lMax=height[l]
            area+=lMax-height[l]
            if height[r]>rMax:
                rMax=height[r]
            area+=rMax-height[r]
            if lMax<rMax:
                l+=1
            else:
                r-=1
        return area            