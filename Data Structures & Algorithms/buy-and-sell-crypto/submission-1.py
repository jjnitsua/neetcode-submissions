class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l,r=0,len(prices)-1
        while l<r:
            for i in range(l+1,r+1):
                if prices[i]-prices[l]>profit:
                    profit=prices[i]-prices[l]
            l+=1
        return profit