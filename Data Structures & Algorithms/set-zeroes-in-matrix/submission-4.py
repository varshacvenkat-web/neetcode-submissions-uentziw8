class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        first_row=False
        for c in range(col):
            if matrix[0][c]==0:
                first_row=True
        first_col=False 
        for r in range(row):
            if matrix[r][0]==0:
                first_col=True 
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c]==0:
                    matrix[r][0]=0 #mark at 0th column
                    matrix[0][c]=0 #mark at 0th row 
        for r in range(1,row):
            for c in range(1,col):
                if matrix[0][c]==0 or matrix[r][0]==0: #at all the idnicators we make row column equal 0
                    matrix[r][c]=0
        if first_row:
            for c in range(col):
                matrix[0][c]=0 #column is the otnl thing that chnage
        if first_col:
            for r in range(row):
                matrix[r][0]=0 #row is the only thing that chnages so we set everything in first column to 0
         
        


                    


        
        