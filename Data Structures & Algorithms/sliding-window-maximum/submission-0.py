class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=0
        window=[]
        res=[]
        while r<len(nums):
            if r-l+1<=k:
                window.append(nums[r])
                if r-l+1==k:
                    res.append(max(window))
            else:
                del window[0]
                window.append(nums[r])
                res.append(max(window))
            r+=1

        return res