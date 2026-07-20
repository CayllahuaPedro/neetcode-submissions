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
            count = k
            if char != word[k]:
                return False
            else:
                count = k+1
            visited.add((i,j))
            res = (recuExist(i+1, j, count) or recuExist(i, j+1, count) 
            or recuExist(i-1, j, count) or recuExist(i, j-1, count))
            if not res:
                visited.remove((i,j))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if recuExist(i,j, 0):
                    return True
        return False