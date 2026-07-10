# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    preIdx = inIdx = 0
    def dfs(self, limit: float | int, inorder: List[int], preorder:List[int]):
        if self.preIdx >= len(preorder):
            return None
        if inorder[self.inIdx] == limit: 
            self.inIdx+=1
            return None 
        node_val = preorder[self.preIdx]
        self.preIdx+=1
        node = TreeNode(node_val)
        node.left = self.dfs(node_val, inorder, preorder)
        node.right = self.dfs(limit, inorder, preorder)
        return node
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(math.inf, inorder, preorder)
        