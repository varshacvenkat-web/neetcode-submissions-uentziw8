class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        def dp(n):
            if n==0:
                return nums[0]
            if n==1:
                return max(nums[1],nums[0])
            if n in cache:
                return cache[n]
            cache[n]=max((nums[n]+dp(n-2)),dp(n-1))
            return cache[n]
        return dp(len(nums)-1)
            

     