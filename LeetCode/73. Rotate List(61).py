# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        l = 1
        last = head
        while last.next != None:
            last = last.next
            l += 1

        last.next = head

        k = k % l

        curr = head
        for i in range(l - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None

        return new_head
