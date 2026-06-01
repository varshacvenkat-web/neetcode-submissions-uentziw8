class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results={}
        for i in nums:
            if i in results:
                results[i]=results[i]+1
            else:
                results[i]=1
        sorted_key=sorted(results,key=lambda x: results[x])
        return sorted_key[-k:]
            

        