class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda i:i[0])
        mins=intervals[0][0] #sets min to first number in first interval after sort
        maxs=intervals[0][1] #sets max to second number in first interval after sort 
        result=[]
        for i in intervals[1:]:
            start=i[0]
            end=i[-1]
            if start<=maxs:
                maxs=max(maxs,end)
                #result.append([mins,maxs])
            else:
                result.append([mins,maxs])
                mins=start
                maxs=end
        result.append([mins,maxs])
        return result 

                     
        