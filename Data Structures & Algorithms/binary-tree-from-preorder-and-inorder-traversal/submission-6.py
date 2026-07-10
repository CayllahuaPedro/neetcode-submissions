# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = preorder[0]
        subTreeRoot= TreeNode(root)
        rootIdx= inorder.index(root) # posicion del root en inorder
        leftSubTree = inorder[:rootIdx]
        rightSubTree = inorder[rootIdx+1:]
        subTreeRoot.left = self.buildTree(preorder=preorder[1:], inorder= leftSubTree)
        subTreeRoot.right = self.buildTree(preorder=preorder[len(leftSubTree)+1:], inorder=rightSubTree) 
        return subTreeRoot