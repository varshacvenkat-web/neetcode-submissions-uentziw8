class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for layer in range(n//2):
            first=layer
            last=n-1-layer
            for i in range(first,last):
                top = matrix[first][i]
                right = matrix[i][last]
                bottom = matrix[last][n-1-i]
                left = matrix[n-1-i][first]

                matrix[first][i] = left
                matrix[i][last] = top
                matrix[last][n-1-i] = right
                matrix[n-1-i][first] = bottom
    


