class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #0 will become 3 len(s)-1-i
        #1 will become 2. 4-1-1=2
        #2 will beocome 1 4-1-2=1
        #3 will become 0.  4-1-0=3
        for i in range((len(s))//2):
            x=len(s)-1-i #saving pos
            z=s[i]
            y=s[x]
            s[i]=y #setting s[i] to new s[x] position
            s[x]=z #setting s[x] to new s[i] position
        return s
        #so in i=0 we replace s[3]=s[0] and then s[0]=s[3]
        #so in n,e,e,t it becomes t,e,e,n
        #in i=3 we replace s[0]=s[3] n,e,e.n