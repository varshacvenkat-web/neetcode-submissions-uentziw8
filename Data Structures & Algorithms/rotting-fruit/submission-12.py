class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=(len(grid),len(grid[0]))
        visit=set()
        queue=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    queue.append((r,c))
                    visit.add((r,c))
        minute=0
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in neighbors:
                    if min(dr+r,dc+c)<0 or dr+r==ROWS or dc+c==COLS or (dr+r,dc+c) in visit or grid[dr+r][dc+c]==0:
                        continue 
                    if grid[dr+r][dc+c]==1:
                        queue.append((dr+r,dc+c))
                        visit.add((dr+r,dc+c))
            if queue:
                minute+=1 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visit:
                    return -1 
        return minute         
        