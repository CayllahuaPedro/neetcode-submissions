# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root: Optional[TreeNode]):
            nonlocal res
            if not root:
                res.append("null")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        def buildDfs(root: str):
            nonlocal values
            if not root: 
                return None
            if root == "null":
                return None
            rootNode = TreeNode(int(root))
            if len(values) > 0:
                rootNode.left = buildDfs(values.pop(0))
            else:
                return None
            if len(values) > 0:
                rootNode.right = buildDfs(values.pop(0))
            else:
                return None
            return rootNode
        rootSol = values.pop(0)
        return buildDfs(rootSol)