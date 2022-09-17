# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        
        def count_height(root):
            if not root:
                return 0
            
            left_count = count_height(root.left)
            right_count = count_height(root.right)
            
            if abs(left_count - right_count) > 1:
                self.is_balanced = False
            
            return 1 + max(left_count,right_count)
        
        count_height(root)
        
        return self.is_balanced