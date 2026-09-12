import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(b / mid) for b in piles) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo