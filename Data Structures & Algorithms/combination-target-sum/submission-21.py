class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results=[]
        queue = deque([[0, [], target]]) #start state: index 0, empty, fu

        while queue:
            start=queue.popleft()

            i=start[0]
            subset=start[1]
            remaining=start[2] #keeps remaiing at the target value across iteraiotns since we just popped the first value 

            if remaining==0:
                results.append(subset)
            
            elif i==len(nums) or remaining<0:
                pass 
            
            else:
                num=nums[i]
                queue.append([i,subset+[num],remaining-num]) #we add current index again, add same num to existing subset, and then subtract remaining 
                queue.append([i+1,subset,remaining]) #we move onto next index, new subset, and remaining starts over 
        return results 