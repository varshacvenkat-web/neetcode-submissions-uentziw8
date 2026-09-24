class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top,bottom=0,len(matrix)-1 #top is 0 pointer, bottom is bototm row pointer
        left,right=0, len(matrix[0])-1 #leftmost colum, rightmost colummn

        while top<=bottom and left<=right:
            #top row left to right
            for i in range(left,right+1):
                res.append(matrix[top][i]) #add the top row from left to right 
            top+=1

            #right column, top to bottom
            for r in range(top,bottom+1):
                res.append(matrix[r][right]) #add the right col from top to bottom
            right-=1
            
            if top<=bottom:
                for x in range(right,left-1,-1):
                    res.append(matrix[bottom][x]) #add the bottom row from rigth to left 
                bottom-=1
            if left<=right:
                for j in range(bottom,top-1,-1):
                    res.append(matrix[j][left])
                left+=1
        return res 
            


        