class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS,COLS=(len(image),len(image[0]))
        visit=set()
        original=image[sr][sc]
        if original==color:
            return image 
        def dfs(r,c):
            if min(r,c)<0 or (r==ROWS or c==COLS) or (r,c) in visit or image[r][c]!=original: 
                return 0
            visit.add((r,c))
            image[r][c]=color 
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        dfs(sr,sc)
        return image 
       
    
