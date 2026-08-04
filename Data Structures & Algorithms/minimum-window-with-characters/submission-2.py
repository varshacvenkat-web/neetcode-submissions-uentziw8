class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts={}
        window={}
        left=0
        best=""
        for i in t:
            counts[i]=counts.get(i,0)+1
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            valid=True 
            for x in counts:
                if window.get(x,0)<counts[x]:
                    valid=False 
                
            while valid:
                if best=="" or len(s[left:right+1])<len(best):
                    best=s[left:right+1]
            
                window[s[left]]=window.get(s[left],0)-1 #removing freq from windows
                left+=1
                for x in counts:
                    if window.get(x,0)<counts[x]:
                        valid=False 
        return best 
              
              

        