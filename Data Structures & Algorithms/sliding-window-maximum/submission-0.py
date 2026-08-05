class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        right=left+k
        maxs=[]
        for left in range(len(nums)):
            if left>len(nums)-k:
                break

                
            maxs.append(max(nums[left:right]))
            right+=1
        return maxs

            
        