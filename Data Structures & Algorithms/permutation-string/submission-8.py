class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        s1dict={}
        s2dict={}
        for i in s1:
            s1dict[i]=s1dict.get(i,0)+1
        for i in range(len(s2)):
            s2dict[s2[i]]=s2dict.get(s2[i],0)+1
            if i-left+1>len(s1):
                left+=1
                s2dict[s2[left-1]]=s2dict.get(s2[left-1],0)-1
                if s2dict[s2[left-1]]==0:
                    del s2dict[s2[left-1]]
            if s1dict==s2dict:
                return True 
        return False 