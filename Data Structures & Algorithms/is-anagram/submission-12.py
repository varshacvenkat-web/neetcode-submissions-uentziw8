class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict={}
        tdict={}
        for i in s:
            if i in sdict:
                sdict[i]=sdict.get(i,0)+1
            else:
                sdict[i]=1
        for x in t:
            if x in tdict:
                tdict[x]=tdict.get(x,0)+1
            else:
                tdict[x]=1
        if sdict==tdict:
            return True 
        else:
            return False 
