import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        results=[]
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        while k>0:
            x=heapq.heappop(heap)
            results.append(-x)
            k-=1
        return results[-1]

        