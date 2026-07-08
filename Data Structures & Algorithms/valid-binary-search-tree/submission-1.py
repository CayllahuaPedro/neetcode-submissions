# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def inOrder(self, root, res):
        if not root: 
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res =[]
        self.inOrder(root, res)
        curr=-math.inf
        for num in res:
           if num > curr:
            curr = num
           else:
            return False
        return True