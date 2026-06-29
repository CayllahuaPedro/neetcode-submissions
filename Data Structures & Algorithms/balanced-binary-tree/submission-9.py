# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node: Optional[TreeNode])-> int:
        if not node:
            return 0
        leftTree = 0
        rightTree = 0
        if node.left:
            leftTree = self.height(node.left) 
        if node.right:
            rightTree = self.height(node.right)
        return 1+ max(leftTree,rightTree)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        leftTree= self.height(root.left) if root and root.left else 0
        rightTree= self.height(root.right) if root and root.right else 0
        return abs(leftTree-rightTree) <=1 and (self.isBalanced(root.left) if root and root.left else True) and (self.isBalanced(root.right) if root and root.right else True)