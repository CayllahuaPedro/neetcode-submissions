class TrieNode:
    def __init__(self):
        self.children = {}
        self.word : Optional[str] = None
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        current = self.root 
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found = [] #palabras encontradas
        wDict = WordDictionary()

        for word in words:
            wDict.addWord(word)
        def findWordRecu(i: int, j:int, current: TrieNode):
            if i > len(board) -1 or i < 0:
                return 
            if j > len(board[0])-1 or j < 0:
                return 
            if (i,j) in visited:
                return 
            char = board[i][j]
            if char not in current.children:
                return 
            current = current.children[char]
            if current.word is not None:
                found.append(current.word)
                current.word= None
            visited.add((i,j))
            findWordRecu(i+1, j, current)
            findWordRecu(i-1, j, current)
            findWordRecu(i,j +1, current)
            findWordRecu(i, j-1,current)
            visited.remove((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                current = wDict.root
                findWordRecu(i,j, current)
        return found