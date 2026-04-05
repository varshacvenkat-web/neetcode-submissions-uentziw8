class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[]
        def dfs(i,subset:List[int]):
            if i==len(nums):
                results.append(subset)
                return 
            else:
                dfs(i+1, subset+[nums[i]])
                dfs(i+1,subset)
        dfs(0,[])
        return results 

            

        
    


        