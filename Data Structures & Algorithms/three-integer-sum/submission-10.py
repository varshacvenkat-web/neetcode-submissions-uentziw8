class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while i<j<k and [i]!=[j]!=[k]:
                if nums[i]+nums[j]+nums[k]==0:
                    output.add((nums[i],nums[j],nums[k]))
                    k=k-1
                    j=j+1
                if nums[i]+nums[j]+nums[k]>0:
                    k=k-1
                if nums[i]+nums[j]+nums[k]<0:
                    j=j+1
        result=[]
        for x in output:
            result.append(list(x))
        return result