# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1=""
        
        while head!=None:
            str1+=str(head.val)
            head=head.next
        if str1==str1[::-1]:
            return True
        return False
            