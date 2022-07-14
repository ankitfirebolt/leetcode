# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        merged_list = ListNode()
        
        if list1.val < list2.val:
            merged_list.val = list1.val
            list1 = list1.next
        else:
            merged_list.val = list2.val
            list2 = list2.next
            
        merged_list.next = self.mergeTwoLists(list1, list2)
        return merged_list