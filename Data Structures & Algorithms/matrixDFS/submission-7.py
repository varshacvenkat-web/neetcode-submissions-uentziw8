class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW,COLS=len(grid),len(grid[0]) #defines length of row and colummn
        visit=set() #creates the already visited set 
        return self.dfs(grid,0,0,visit,ROW,COLS)
    def dfs(self,grid,r,c,visit,ROW,COLS): #we pass grid, Row column pair, and laready vsiited set into dfs
        if min(r,c)<0 or (r==ROW or c==COLS) or ((r,c) in visit) or (grid[r][c]==1):
            return 0
        elif r==ROW-1 and c==COLS-1:
            return 1
        visit.add((r,c))

        count=0
        count+=self.dfs(grid,r+1,c,visit,ROW,COLS)
        count+=self.dfs(grid,r,c+1,visit,ROW,COLS)
        count+=self.dfs(grid,r-1,c,visit,ROW,COLS)
        count+=self.dfs(grid,r,c-1,visit,ROW,COLS)
        visit.remove((r,c))
        return count 

