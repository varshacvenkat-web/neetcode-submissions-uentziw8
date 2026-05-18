class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevrow=[0]*n
        for m in range(m-1,-1,-1):
            currow=[0]*n
            currow[n-1]=1
            for r in range(n-2,-1,-1):
                currow[r]=currow[r+1]+prevrow[r]
            prevrow=currow
        return currow[0]
        