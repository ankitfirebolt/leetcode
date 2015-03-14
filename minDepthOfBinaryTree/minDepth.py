# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right != None:
            return 1+self.minDepth(root.right)
        elif root.left != None and root.right == None:
            return 1+self.minDepth(root.left)
        else:
            return min(1+self.minDepth(root.left), 1+self.minDepth(root.right))
