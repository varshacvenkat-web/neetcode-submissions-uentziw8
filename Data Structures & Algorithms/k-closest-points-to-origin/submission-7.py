import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results=[]
        heap=[]
        for x,y in points:
            heapq.heappush(heap,((x**2)+(y**2),[x,y]))
        while k>0:
            x=heapq.heappop(heap) #until k=-len(heap)
            results.append(x[1])
            k-=1
        return results
