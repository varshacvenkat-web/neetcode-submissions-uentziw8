class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=nums[-1]
        current=0
        for i in range(len(nums)):
            current=max(nums[i],nums[i]+current) #at each it. wheter to reset or take sum
            maxs=max(maxs,current) #finds max amognst iteraton and saves 
        return maxs