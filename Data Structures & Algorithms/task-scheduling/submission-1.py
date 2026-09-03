from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts=Counter(tasks) #frequency counter 
        maxFreq=max(counts.values()) #max of the values
        numtasksatmaxfreq=0 #checker for the last row
        for i in counts.values():
            if i==maxFreq:
                numtasksatmaxfreq+=1 
        formula=(maxFreq-1)*(n+1)+numtasksatmaxfreq
        return max(len(tasks),formula)



        