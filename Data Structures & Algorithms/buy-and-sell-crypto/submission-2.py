class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pmax=0
        pmin=float('inf')
        for p in prices:
            pmin=min(p,pmin)
            pmax=max(pmax,p-pmin)
        return int(pmax)