class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results=[]
        def dfs(i,subset=list,target=int):
            if target==0: 
                results.append(subset)
                return
            if target<0 or i==len(nums):
                return 
            dfs(i,subset+[nums[i]],target-nums[i])
            dfs(i+1,subset,target)
        dfs(0,[],target)
        return results 
        