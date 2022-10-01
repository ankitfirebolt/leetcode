# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return True
        
        self.front_pointer = head
        self.ans = True
        
        def recurse(head):
            
            if not head:
                return
            else:
                recurse(head.next)
                self.ans = self.ans and (self.front_pointer.val == head.val)
                self.front_pointer = self.front_pointer.next
                return
        
        recurse(head)
        return self.ans