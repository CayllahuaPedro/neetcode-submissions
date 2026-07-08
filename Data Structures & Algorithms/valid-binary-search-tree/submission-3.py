# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidRecu(self, root: Optional[TreeNode], range: tuple[float, float]) -> bool:
        if not root:
            return True
        if range[0] < root.val < range[1]:
            return self.isValidRecu(root.right, (root.val, range[1])) and self.isValidRecu(
                root.left, (range[0], root.val)
            )
        else:
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidRecu(root, (-math.inf, math.inf))
