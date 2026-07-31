class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0 
        maxfreq=0
        s1dict={}
        count={}
        for i in s1:
            s1dict[i]=s1dict.get(i,0)+ 1
        for right in range(len((s2))):
            count[s2[right]]=count.get(s2[right],0)+1 #increase count
            if right-left+1>len(s1):
                left+=1
                count[s2[left-1]]=count.get(((s2[left-1])))-1
                if count[s2[left-1]]==0:
                    del count[s2[left-1]]
            if s1dict==count:
                return True 

        return False 
        