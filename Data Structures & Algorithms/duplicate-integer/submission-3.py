class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets={}
        for i in nums:
            sets[i]=sets.get(i,0)+1
        for i in nums:
            if sets[i]>1:
                return True 
        return False 

        