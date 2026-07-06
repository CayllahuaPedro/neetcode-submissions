# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []
        res = []
        stack = deque([root])
        while len(stack) > 0:
            level = []
            level_size = len(stack)
            for _ in range(level_size):
                node = stack.popleft()
                level.append(node.val)
                if node.left is not None: 
                    stack.append(node.left)
                if node.right is not None: 
                    stack.append(node.right)
            res.append(level[-1])
        return res