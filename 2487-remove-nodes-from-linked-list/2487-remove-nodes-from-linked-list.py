# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(n: ListNode) -> ListNode:
            tail = None
            while n:
                nxt = n.next
                n.next = tail
                tail = n
                n = nxt
            return tail

        cur = tail = reverse(head)
        mx = cur.val
        while cur.next:
            if cur.next.val < mx:
                cur.next = cur.next.next
            else:
                cur = cur.next
                mx = cur.val
        return reverse(tail)