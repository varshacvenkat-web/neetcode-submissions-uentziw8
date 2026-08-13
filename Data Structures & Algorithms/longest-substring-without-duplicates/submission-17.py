class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={} #dicitonary
        left=0 #left poitner
        best=0 #base pointer 
        for right in range(len(s)): #iterate through s with right pointer 
            if s[right] in seen and seen[s[right]]>=left: #we check seen for the last updated psoition of right, and see if it within the window from L to Right 
                left=seen[s[right]]+1 #if it is within the window we move left to one after the last duplicate position
            seen[s[right]]=right  #we update the right position at each iteration
            best=max(best,right-left+1) #return the max window inclusive of the left and right characters 
        return best  #return ebst 




            


        
        