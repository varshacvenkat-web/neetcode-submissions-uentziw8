class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1

        while left<right:
            mid=((left+right))//2
        
            if nums[right]<nums[mid]:
                left=mid+1 #start at beginning of right half
            else:
                right=mid #starts at end of left half 
        return nums[left]
        