# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        
        def count_diameter(root):
            if not root:
                return 0
            
            left_count = 1 + count_diameter(root.left)
            right_count = 1 + count_diameter(root.right)
            
            total_edges = left_count + right_count - 2
            
            self.diameter = max(total_edges, self.diameter)
            
            return max(left_count, right_count)
        
        count_diameter(root)
        return self.diameter
                