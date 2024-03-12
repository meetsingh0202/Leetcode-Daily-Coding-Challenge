# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = head
        arr = []
        HashMap = dict()
        currSum = 0
        while head:
            currSum += head.val
            if currSum in HashMap:
                newHashMap = dict()
                for key, val in HashMap.items():
                    newHashMap[key] = val
                    if key == currSum:
                        break
                HashMap = newHashMap
                temp = newHashMap[currSum]
                temp.next = head.next
                head = head.next
                continue
            if currSum == 0:
                newhead = head.next
                head1 = newhead
                del head
                head = newhead
                HashMap = dict()
                continue
            HashMap[currSum] = head
            head = head.next
        return head1