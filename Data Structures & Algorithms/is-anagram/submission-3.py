class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapA={}
        hashmapB={}
        for i in s:
            if i not in hashmapA:
                hashmapA[i]=1
            else:
                hashmapA[i]+=1
        for x in t:
            if x not in hashmapB:
                hashmapB[x]=1
            else:
                hashmapB[x]+=1
        if hashmapA==hashmapB:
            return True
        else:
            return False 