class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            val = [0]*9
            for j in range(9):
                if board[i][j]!=".":
                    val[int(board[i][j])-1]+=1
            for k in val:
                if k>1:
                    return False
        for i in range(9):
            val = [0]*9
            for j in range(9):
                if board[j][i]!=".":
                    val[int(board[j][i])-1]+=1
            for k in val:
                if k>1:
                    return False
        for x in range(0,8,3):
            for y in range(0,8,3):
                val = [0]*9
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if board[j][i]!=".":
                            val[int(board[j][i])-1]+=1
                for k in val:
                    if k>1:
                        return False
        return True

                