import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:  
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)    
            if -x!=-y:
                heapq.heappush(heap,(x-y))
        return -heapq.heappop(heap) if heap else 0
         

        