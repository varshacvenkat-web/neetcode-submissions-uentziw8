class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        best=0
        left=0
        for right in range(len(s)):
            if s[right] in seen:
                x=seen[s[right]]
                if seen[s[right]]>=left:
                    left=x+1
            seen[s[right]]=right
            best=max(best,right-left+1)
        return best
        