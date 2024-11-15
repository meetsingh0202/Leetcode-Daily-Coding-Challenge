# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        def merge(left, right):
            
            dummy = ListNode(-1)
            temp = dummy
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    temp = temp.next
                    left = left.next
                else:
                    temp.next = right
                    temp = temp.next
                    right = right.next
                    
            while left:
                temp.next = left
                temp = temp.next
                left = left.next
                
            while right:
                temp.next = right
                temp = temp.next
                right = right.next
                
            return dummy.next
        
        def mergeSort(lists, start, end):
            if start == end:
                return lists[start]
            
            mid = (start + end) >> 1
            left = mergeSort(lists, start, mid)
            right = mergeSort(lists, mid + 1, end)
            
            return merge(left, right)
        
        if not lists:
            return None
        return mergeSort(lists, 0, len(lists) - 1)

