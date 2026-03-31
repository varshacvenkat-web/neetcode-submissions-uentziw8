class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low <= high:
            k=((low+high))//2
            total=0
            for i in piles:
                total += math.ceil((i/k))
            if total<=h:
                high=k-1
                result=k
            elif total>h:
                low=k+1
        return result 
       


        