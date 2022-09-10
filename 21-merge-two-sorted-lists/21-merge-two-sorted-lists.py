# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode()
        curr = dummy_head #this is the tail
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(val=list1.val, next=None)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(val=list2.val)
                curr = curr.next
                list2 = list2.next                
                
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy_head.next