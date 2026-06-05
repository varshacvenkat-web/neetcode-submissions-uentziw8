class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for i in s:
            if i.isalnum():
                cleaned+=i
        cleaned=cleaned.lower()
        for i in range(len(cleaned)):
            if cleaned[i]!=cleaned[-i-1]: 
                return False
        return True       