class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        foundRowIdx = -1
        top, bottom = 0, n-1
        while top <= bottom:
            middle = (top+bottom) // 2
            if target == matrix[middle][0]:
                return True
            if target < matrix[middle][0]:
                bottom = middle -1
            else: 
                foundRowIdx= middle #aca se actualiza el mejor candidato? 
                top = middle + 1
        if foundRowIdx == -1:
            return False
        left, right = 0, m-1
        foundRow = matrix[foundRowIdx]
        while left <= right:
            middle = (left + right) // 2
            if target == foundRow[middle]:
                return True
            if target < foundRow[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return False
