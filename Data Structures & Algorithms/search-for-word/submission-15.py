class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def recuExist(i: int, j:int, k: int) -> bool:
            if (i, j) in visited:
                return False
            else:
                visited.add((i,j))
            if i > len(board) -1 or i < 0:
                return False
            if j > len(board[0]) -1 or j < 0:
                return False
            char = board[i][j]
            if k == len(word)-1 and word[k] == char:
                return True
            count = k
            if char != word[k]:
                if (i,j) in visited: 
                    visited.remove((i,j)) 
                return False
            else:
                count = k+1
            res =(recuExist(i+1, j, count) or recuExist(i, j+1, count) 
            or recuExist(i-1, j, count) or recuExist(i, j-1, count))
            if not res:
                if (i,j) in visited:
                    visited.remove((i,j))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if recuExist(i,j, 0):
                    return True
        return False