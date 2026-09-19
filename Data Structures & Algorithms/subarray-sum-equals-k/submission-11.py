class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict={0:1}
        count=0
        runningsum=0
        for i in range(len(nums)):
            runningsum+=nums[i]
            target=runningsum-k
            if target in dict:
                count+=dict[target]
            if runningsum not in dict:
                dict[runningsum]=1
            else:
                dict[runningsum]+=1
        return count 
            

        