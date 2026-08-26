class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdict={} #dictionary for t 
        sdict={} #dictionary for s 
        left=0
        matched=0
        best=""
        valid=False 
        for i in t:
            tdict[i]=tdict.get(i,0)+1
        for j in range(len(s)):
            sdict[s[j]]=sdict.get(s[j],0)+1
            if s[j] in tdict:
                if sdict[s[j]]==tdict[s[j]]:
                    matched+=1
                if matched==len(tdict):
                    valid=True 
            while valid:
                if best=="" or len(s[left:j+1])<len(best):
                    best=s[left:j+1]
                if s[left] in tdict:
                    if sdict[s[left]]==tdict[s[left]]:
                        matched-=1
                        sdict[s[left]]=sdict.get(s[left],0)-1
                        left+=1
                        valid=False
                    else:
                        sdict[s[left]]=sdict.get(s[left],0)-1
                        left+=1
                        valid=True

                else:
                    sdict[s[left]]=sdict.get(s[left],0)-1
                    left+=1
                    valid=True       
        return best 
        

        