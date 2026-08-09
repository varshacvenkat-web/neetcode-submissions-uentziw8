class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxs=0
        low=max(prices)
        diff=0
        i=0
        for i in range(len(prices)):
            low=min(low,prices[i])
            #maxs=max(maxs,prices[i])
            diff=max(diff,prices[i]-low)
        return diff 