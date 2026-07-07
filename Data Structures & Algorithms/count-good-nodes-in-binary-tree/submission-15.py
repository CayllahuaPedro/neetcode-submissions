# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from collections import deque


class Solution:
    def goodNodesRecu(self, root: TreeNode, maxValue: int | float = -math.inf) -> int:
        if not root:
            return 0
        res = 0
        maxCurrent = max(maxValue, root.val)
        leftTree = self.goodNodesRecu(root.left, maxCurrent)
        rightTree = self.goodNodesRecu(root.right, maxCurrent)
        if root.val >= maxValue:
            res = 1 + leftTree + rightTree
        else:
            res = leftTree + rightTree
        return res

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesRecu(root)
