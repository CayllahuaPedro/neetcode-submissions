# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr: 
         #aca va a hasta el fondo a la izq ok.. 
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() #saco el ultimo nodo que meti
            k -= 1 #procesa el nodo
            if k==0:
                #quiere dcir que ya procesamos k nodos
                return curr.val
            curr = curr.right #voy a la rama derecha