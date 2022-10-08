# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        elif (not root and subRoot) or (root and not subRoot):
            return False

        
        def is_equal(root, subRoot):
            if not root and not subRoot:
                return True
            elif (not root and subRoot) or (root and not subRoot):
                return False
            elif root.val != subRoot.val:
                return False
            else:
                return is_equal(root.left, subRoot.left) and is_equal(root.right, subRoot.right)
        
        
            
        return is_equal(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
