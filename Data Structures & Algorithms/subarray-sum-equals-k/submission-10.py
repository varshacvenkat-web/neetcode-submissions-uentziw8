class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict={0:1}
        count=0
        prefixnums=0
        for i in range(len(nums)):
            prefixnums+=nums[i] #update prefixnums
            target=prefixnums-k
            if target in dict:
                count+=dict[target]
            if prefixnums not in dict:
                dict[prefixnums]=1
            else:
                dict[prefixnums]+=1
        return count
            
            

        