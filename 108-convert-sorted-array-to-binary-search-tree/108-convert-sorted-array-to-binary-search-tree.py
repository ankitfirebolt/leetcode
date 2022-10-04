# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        mid_index = len(nums)//2
        root = TreeNode(val = nums[mid_index])
        root.left = self.sortedArrayToBST(nums[0:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index+1:])
        return root