# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow
        nxt=None
        prev=None
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        a1=head
        a2=prev
        while a2!=None:
            if a1.val!=a2.val:
                return False
            a1=a1.next
            a2=a2.next
        return True
