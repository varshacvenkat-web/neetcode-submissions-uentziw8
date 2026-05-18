class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            rows=len(obstacleGrid)
            cols=len(obstacleGrid[0])
            prevrow=[0]*cols
            for r in range(rows-1,-1,-1):
                currow=[0]*cols
                if obstacleGrid[r][cols-1]==1: #obstacle
                    currow[cols-1]=0
                elif r==rows-1: #last tile
                    currow[cols-1]=1
                else:
                    currow[cols-1]=prevrow[cols-1]
                for c in range(cols-2,-1,-1):
                    if obstacleGrid[r][c]==1:
                        currow[c]=0
                    elif obstacleGrid[r][c]==0:
                        currow[c]=currow[c+1]+prevrow[c]
                prevrow=currow
                
            return prevrow[0]

        