class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        mins=newInterval[0]
        maxs=newInterval[1]
        result=[]
        placed=False 
        for i in intervals:
            start=i[0]
            end=i[-1]
            if end<mins:
                result.append([start,end])
            elif start>maxs:
                result.append([mins,maxs])
                mins=start
                maxs=end 
            else: 
                mins=min(mins,start)
                maxs=max(maxs,end)
        result.append([mins,maxs])
        return result


            


        