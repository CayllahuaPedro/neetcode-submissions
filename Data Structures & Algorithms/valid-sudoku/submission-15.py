class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n : int  = len(board)
        colDuplicates =  [set() for _ in range(n)]
        squareDuplicates = [set() for _ in range(9)]
        for i in range(0, n):
            rowDuplicates = set() # row
            for j in range(0,n): #check for row duplicates
                colDict = colDuplicates[j] # columm 
                squareNumber= ( i // 3 ) * 3 + (j// 3)
                squareDict = squareDuplicates[squareNumber]
                numStr = board[i][j]
                if numStr.isdigit(): 
                    num = int(numStr)
                    if num in colDict: return False
                    if num in rowDuplicates : return False
                    if num in squareDict : return False
                    colDict.add(num)
                    rowDuplicates.add(num)
                    squareDict.add(num)

        return True

