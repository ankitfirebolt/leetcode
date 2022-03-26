# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def helper(root, left_count = 0, right_count = 0, depth=0, memo = {}):
            if not root:
                return

            key = right_count - left_count
            if key not in memo:
                memo[key] = [[depth, root.val]]
            else:
                memo[key] = memo[key]+[[depth, root.val]]

            helper(root.left, left_count+1, right_count, depth+1, memo)
            helper(root.right, left_count, right_count+1, depth+1, memo)
           
            sorted_keys = sorted(memo.keys()) #will sort first by left_count-right_count, and then by depth
            sorted_memo = [memo[k] for k in sorted_keys]
            
            for i,x in enumerate(sorted_memo):
                sorted_memo[i] = [y[1] for y in sorted(x, key=lambda k: k[0])]
            return sorted_memo
        return helper(root)