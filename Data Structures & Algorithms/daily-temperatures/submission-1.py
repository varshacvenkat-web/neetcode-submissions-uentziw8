class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[]
        for i in range(len(temperatures)):
            j=i+1
            while j<len(temperatures):
                if temperatures[j]>temperatures[i]:
                    x=j-i
                    output.append(x)
                    break 
                elif temperatures[j]<=temperatures[i]:
                    j=j+1
            if j==len(temperatures):
                output.append(0)

        return output
            
        