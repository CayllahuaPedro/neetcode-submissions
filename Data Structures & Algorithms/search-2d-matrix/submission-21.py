class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS-1 
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] > target:
                bottom = row -1 
            elif matrix[row][-1] < target:
                top = row+1
            else:
               break
        if not (top <= bottom):
            return False
        left, right = 0, COLS-1
        row = (top + bottom) //2
        while left <= right:
            column = (left + right) // 2
            if matrix[row][column] == target:
                return True
            if matrix[row][column] < target:
                        left= column + 1
            else:
                right = column -1
        return False
                

