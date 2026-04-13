class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapA={}
        for i in s:
            if i not in hashmapA:
                hashmapA[i]=1
            else:
                hashmapA[i]+=1
        for i in t:
            if i not in hashmapA:
                return False 
            else:
                hashmapA[i]-=1
        for i in hashmapA:
            if hashmapA[i]!=0:
                return False
        return True 
       