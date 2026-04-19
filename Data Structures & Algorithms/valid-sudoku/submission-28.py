class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n : int  = len(board)
        colMaskArray = [0] * n
        squareMaskArray = [0] * n
        for i in range(0, n):
            rowMask = 0
            for j in range(0,n): #check for row duplicates
                colMask = colMaskArray[j] 
                squareNumber= ( i // 3 ) * 3 + (j// 3)
                squareMask = squareMaskArray[squareNumber]
                numStr = board[i][j]
                if numStr.isdigit(): 
                    num = int(numStr)
                    if colMask & (1 << num): return False
                    if rowMask & (1 << num): return False
                    if squareMask & (1 << num ): return False
                    squareMask = squareMask | (1 << num)
                    rowMask = rowMask | (1 << num)
                    colMask = colMask | (1 << num)
                    colMaskArray[j] = colMask
                    squareMaskArray[squareNumber] = squareMask
        return True

