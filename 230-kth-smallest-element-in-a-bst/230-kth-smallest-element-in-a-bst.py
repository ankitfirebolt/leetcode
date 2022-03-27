# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        ans = None
        count = 0
        
        def helper(root):
            if not root:
                return []
            return helper(root.left) + [root.val] + helper(root.right)
        
        inorder_traversal = helper(root)
        return inorder_traversal[k-1]