from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n : int  = len(board)
        colDuplicates =  [defaultdict(int) for _ in range(n)]
        squareDuplicates = [defaultdict(int) for _ in range(9)]
        
        for i in range(0, n):
            rowDuplicates = defaultdict(int) # row
            for j in range(0,n): #check for row duplicates
                colDict = colDuplicates[j] # columm 
                squareNumber= ( i // 3 ) * 3 + (j// 3)
                squareDict = squareDuplicates[squareNumber]
                numStr = board[i][j]
                if numStr.isdigit(): 
                    num = int(numStr)
                    colDict[num]+=1
                    rowDuplicates[num]+= 1
                    squareDict[num]+= 1
                    for num, freq in colDict.items():
                        if freq > 1 : return False
                    if rowDuplicates[num] > 1 : return False
                    if squareDict[num] > 1 : return False

        return True

