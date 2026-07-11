# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), type_check_only:
#         self.val = val
#         self.left = left
#         self.right = right

import math


class Solution:
    maxCurr: int | float = -math.inf
    def traverse(self, root:Optional[TreeNode])-> int:
        if not root:
            return 0
        leftSubTree = max(0, self.traverse(root.left))
        rightSubTree = max(0, self.traverse(root.right))
        self.maxCurr = max(self.maxCurr, leftSubTree+ rightSubTree + root.val, root.val, root.val + leftSubTree, root.val + rightSubTree)
        return root.val +  max(leftSubTree, rightSubTree)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.maxCurr if type(self.maxCurr) is int else 0
       
