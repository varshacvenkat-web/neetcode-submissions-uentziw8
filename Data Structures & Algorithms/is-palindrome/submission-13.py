class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        x=[]
        for i in s:
            if i.isalnum():
                x.append(i)
        for z in range(len(x)):
            if x[z]!=x[-z-1]:
                return False
        return True 