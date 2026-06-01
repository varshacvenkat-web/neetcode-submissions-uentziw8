class Solution:

    def encode(self, strs: List[str]) -> str:
        results=""
        for i in strs:
            results+=str(len(i))+"#"+i
        return results 
    

    def decode(self, s: str) -> List[str]:
        i=0
        results=[]
        while i<len(s):
            j=s.index("#",i)
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            results.append(word)
            i=j+1+length
        return results 



