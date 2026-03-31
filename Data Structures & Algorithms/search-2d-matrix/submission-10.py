class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        L=0
        R=(m*n)-1
        while L <= R:
            mid=((L+R))//2 
            if target > matrix[mid//n][mid%n]:
                L=mid+1 
            elif target < matrix[mid//n][mid%n]:
                R=mid-1
            else:
                return  True 
        return False 