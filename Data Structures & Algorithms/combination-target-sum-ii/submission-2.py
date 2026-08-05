class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results=[]
        start=0
        current_sum=0
        def backtrack(start,current_combo,current_sum):
            if current_sum==target:
                results.append(current_combo[:])
                return 
            if current_sum>target:
                return  
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue 
                current_combo.append(candidates[i])
                current_sum=current_sum+candidates[i]
                backtrack(i+1,current_combo,current_sum)
                current_combo.pop()
                current_sum-=candidates[i]
        backtrack(start,[],current_sum)
        return results 

                

        