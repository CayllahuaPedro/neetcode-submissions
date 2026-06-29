# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maximum = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum =0
        def height(root: Optional[TreeNode])-> int:
            if not root:
                return 0
            leftTree= height(root.left)
            rightTree= height(root.right)
            candidato = leftTree + rightTree
            self.maximum = max(self.maximum ,candidato)
            return 1 + max(leftTree, rightTree)
        height(root)
        return self.maximum