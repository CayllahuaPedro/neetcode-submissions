
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  
        self.is_end_of_word = False


class PrefixTree:
    def __init__(self):   
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            idx = ord(char) - ord('a')

            if current_node.children[idx] is None:
                current_node.children[idx] = TrieNode()
            current_node = current_node.children[idx]

        current_node.is_end_of_word = True
    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if current_node.children[idx] is None:
                return False
            current_node = current_node.children[idx]
        return current_node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if current_node.children[idx] is None:
                return False
            current_node = current_node.children[idx]
        return True
        