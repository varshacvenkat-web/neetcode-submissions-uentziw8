class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n*2
        for i in range(len(nums)):
            ans[0:n]=nums[0:n]
            ans[n:2*n]=nums[0:n]
        return ans

                
                
        