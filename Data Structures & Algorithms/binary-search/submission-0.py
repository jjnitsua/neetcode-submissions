class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if target>nums[-1] or target<nums[0]:
            return -1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
                break
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return -1