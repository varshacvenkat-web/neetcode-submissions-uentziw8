class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)): #j will start one after i 
                x=prices[j]-prices[i] 
                best=max(x,best)
        return best 

    
