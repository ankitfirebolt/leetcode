# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        self.ans = None
        
        def helper(root, p, q):
            
            if not root:
                return False
                
            #recurse first and go all the way to the leaves, then check on the way back
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            
            curr = (root == p) or (root == q) #check for a match in the current node
            
            if (left and right) or (curr and left) or (curr and right):
                self.ans = root
            
            return curr or left or right #if any of these is true, return true for future computations
        
        helper(root, p, q)
        return self.ans