# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def findLength(head):
            tempHead = head
            length = 0
            while tempHead:
                length += 1
                tempHead = tempHead.next
            return length
        
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        
        length = findLength(head)
        currPointer = 0
        secondPointer = head
        
        while currPointer < length // 2:
            secondPointer = secondPointer.next
            currPointer += 1
            
        secondPointer = reverse(secondPointer)
        
        maxSum = float('-inf')
        
        while head and secondPointer:
            maxSum = max(maxSum, head.val + secondPointer.val)
            head = head.next
            secondPointer = secondPointer.next
        
        return maxSum