# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def goodNodes(self, root: TreeNode, max_val: int | float = -math.inf) -> int:
        if not root:
            return 0
        
        # 1 if the current node is "good", else 0
        is_good = 1 if root.val >= max_val else 0
        
        # Update the maximum value seen so far
        max_val = max(max_val, root.val)
        
        # Terminate early by returning the sum immediately
        return is_good + self.goodNodes(root.left, max_val) + self.goodNodes(root.right, max_val)
