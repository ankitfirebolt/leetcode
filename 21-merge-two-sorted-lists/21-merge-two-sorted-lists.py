# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged_list_dummy_head = ListNode()
        merged_list_curr = merged_list_dummy_head
        
        while list1 and list2:
            if list1.val <= list2.val:
                merged_list_curr.next = ListNode(val=list1.val, next=None)
                merged_list_curr = merged_list_curr.next
                list1 = list1.next
            else:
                merged_list_curr.next = ListNode(val=list2.val)
                merged_list_curr = merged_list_curr.next
                list2 = list2.next                
                
        if list1 and not list2:
            merged_list_curr.next = list1
        elif not list1 and list2:
            merged_list_curr.next = list2
        return merged_list_dummy_head.next