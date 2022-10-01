# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def is_mirror(p, q):
            if not p and not q:
                return True
            elif (p and not q) or (not p and q):
                return False
            elif p.val == q.val:
                return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)
            else:
                return False
            
        return is_mirror(root.left, root.right)
                