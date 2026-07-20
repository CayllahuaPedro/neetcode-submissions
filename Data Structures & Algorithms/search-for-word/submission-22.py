class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recuExist(i: int, j:int, k: int) -> bool:
            if i > len(board) -1 or i < 0:
                return False
            if j > len(board[0]) -1 or j < 0:
                return False
            if (i, j) in visited:
                return False
            char = board[i][j]
            if k == len(word)-1 and word[k] == char:
                return True
            if char != word[k]:
                return False
            visited.add((i,j))
            res = (recuExist(i+1, j, k+1) or recuExist(i, j+1, k+1) 
            or recuExist(i-1, j, k+1) or recuExist(i, j-1, k+1))
            if not res:
                visited.remove((i,j))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if recuExist(i,j, 0):
                    return True
        return False