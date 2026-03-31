class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts=[0,0,0]
        for n in nums: #for each value in nums adds that to counts as a tally
            counts[n]+=1
        i=0
        for n in range(len(counts)): #for range from 0-2
            for j in range(counts[n]): #based on repetitive of counts[n]
                nums[i]=n
                i+=1
        return nums



        """
        Do not return anything, modify nums in-place instead.
        """
        