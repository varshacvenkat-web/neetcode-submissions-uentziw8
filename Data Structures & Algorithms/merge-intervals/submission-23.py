class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key= lambda i:i[0]) #sort each list by first number
        mins=intervals[0][0] #the first number in interval
        maxs=intervals[0][-1] #the second number in interval
        result=[]
        for i in  (intervals[1:]):
            start=i[0] #for interval starting @ i[1
            end=i[-1]
            if start<=maxs:
                maxs=max(end,maxs) #start is within interval so we extend
            else: #start is greater than maxs so new interval 
                result.append([mins,maxs]) #append current mins/maxs to result
                mins=start #overwrite mins with new start 
                maxs=end #overwrite max with new end 
                #by overwiritng we can start a new interval block 
        result.append([mins,maxs])
        return result 


        