class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m,k,n=(len(mat1),len(mat1[0]),len(mat2[0])) #len of row of matrix, len of col of matrix 1, len of col of matrix 2
        result=[]
        for i in range(m): #loop trhough row
            result.append([0]*n) #add n columns 
        for q in range(m): #row of mat 1
            for j in range(k): #col of mat1/row of mat 2
                if mat1[q][j]==0:
                    continue 
                else:
                    a=mat1[q][j] #from mat1
                for p in range(n): #col of mat2
                        if mat2[j][p]==0:
                            continue
                        else:
                            b=mat2[j][p] #from mat 2
                            result[q][p]+=a*b #ad
        return result 

        