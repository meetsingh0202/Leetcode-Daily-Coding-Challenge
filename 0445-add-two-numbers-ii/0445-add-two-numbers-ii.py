# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = ''
        
        while l1 != None:
            n1 += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            n2 += str(l2.val)
            l2 = l2.next
            
        n3 = str(int(n1) + int(n2))
        
        head = ListNode(int(n3[0]))
        res = head
        for i in range(1,len(n3)):
            head.next = ListNode( int( n3[i] ) )
            head = head.next
            
        return res