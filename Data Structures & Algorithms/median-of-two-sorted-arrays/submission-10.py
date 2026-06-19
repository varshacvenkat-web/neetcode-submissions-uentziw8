class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            long,short=nums1,nums2
        else:
            long,short=nums2,nums1
        left=0
        right=len(short)
        m=len(short)
        n=len(long)
        while left<=right:
            partition1=((left+right))//2 #finding balance indice in shorter array
            partition2=(((m+n+1))//2)-(partition1) #gives you amount of elements on left side-total amount on 
            #if we hvae short=[1,2,3] we parition to at 1 to make [1] and [2,3]
            #if we have long=[4,5,6,7] partition 2=3, so we have [4,5,6] and [7]
            left1=short[partition1-1] if partition1>0 else float('-inf') #last on left of short(parition 1)
            left2=long[partition2-1] if partition2>0 else float('-inf')#last on left of long(parition 2)=6 in [4,5,6]
            right1=short[partition1] if partition1<len(short) else float ('inf') #first on right of partition 1 in short
            right2=long[partition2] if partition2<len(long) else  float ('inf')#first on right of parition 2=7 [7]
            if max(left1,left2) <= min(right1,right2):#[1,6] compared to [2,7] ensures the bounds amke sense to that left is not greater tahn right 
                if (m+n)%2==1:
                    median=max(left1,left2)
                    return float(median)
                else:
                    median=(max(left1,left2)+min(right1,right2))/2
                    return float(median)
            elif left2>right1: #long left too big, so we need to take more from short [l1,l2,R1,R2]
                left=partition1+1
            else:    
                right=partition1-1                      #left1

