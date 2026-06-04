class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set=[set() for r in range(9)]
        col_set=[set() for c in range(9)]
        box_set={}
        for r in range(9):
            for c in range(9):
                    val=board[r][c]
                    if val == ".":
                        continue 
                    if val in row_set[r] or val in col_set[c]:
                        return False
                    else:
                        row_set[r].add(val)
                        col_set[c].add(val)
                    if (r//3, c//3) not in box_set:
                        box_set[(r//3,c//3)]=set()
                    if val in box_set[(r//3,c//3)]:
                        return False 
                    elif val not in box_set[(r//3,c//3)]:
                        box_set[(r//3,c//3)].add(val) 

        return True 
                        