# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        head1 = ListNode()
        head2 = ListNode()
        
        ptr1 = head1
        ptr2 = head2
        
        while head:
            if head.val < x:
                ptr1.next = ListNode(head.val)
                ptr1 = ptr1.next
            else:
                ptr2.next = ListNode(head.val)
                ptr2 = ptr2.next
                
            head = head.next
        
        ptr1.next = head2.next
        
        return head1.next